import asyncio
import json
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompts.log_prompt import log_prompt, parser
from app.schemas.log_schema import BatchLogResponse, LogResponse
from app.agents import run_planner_agent, run_executor_agent, run_supervisor_agent

# 🔹 Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 🔹 Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 Analyze a single log with fallback
async def analyze_single_log(chain, log: str) -> LogResponse:
    try:
        logger.info(f"Analyzing individual log: {log[:50]}...")
        response = await chain.ainvoke({"logs": log})
        return response  # already a LogResponse (due to parser)

    except Exception as e:
        logger.error(f"Error analyzing log: {str(e)}")
        # 🔥 Fallback to prevent full batch failure
        return LogResponse(
            log_type="unknown",
            attack_type="unknown",
            summary="Error analyzing log",
            suspicious_activity=str(e),
            risk_level="Low",
            confidence_score=0,
            suggested_action="Check system manually"
        )

# 🔹 Batch analysis with parallel execution
async def analyze_logs_batch(logs: list[str]) -> BatchLogResponse:
    logger.info(f"--- Starting Batch Analysis for {len(logs)} logs ---")
    chain = log_prompt | llm | parser

    # 🔥 Run all logs in parallel
    logger.info("Step 1: Running parallel LLM analysis on all logs...")
    tasks = [analyze_single_log(chain, log) for log in logs]
    results = await asyncio.gather(*tasks)
    logger.info(f"Step 1 Completed: Analyzed {len(results)} logs.")

    # 🔹 Aggregation logic
    total = len(results)

    avg_confidence = (
        sum(r.confidence_score for r in results) / total
        if total > 0 else 0
    )

    risk_levels = [r.risk_level for r in results]

    if "High" in risk_levels:
        overall_risk = "High"
    elif "Medium" in risk_levels:
        overall_risk = "Medium"
    else:
        overall_risk = "Low"
    
    logger.info(f"Aggregation: Overall Risk = {overall_risk}, Avg Confidence = {avg_confidence:.2f}")

    # 🔥 Prepare input for Multi-Agent flow
    analysis_data = [r.model_dump() for r in results]
    analysis_results_str = json.dumps({
        "analysis": analysis_data,
        "original_logs": logs
    })
    
    # 🔹 1. Planner Agent
    logger.info("Step 2: Invoking Planner Agent...")
    plan_output = await run_planner_agent(analysis_results_str)
    plan_tasks = plan_output.get("tasks", [])
    logger.info(f"Planner Agent Output: Found {len(plan_tasks)} tasks to execute.")
    for i, task in enumerate(plan_tasks):
        logger.info(f"  - Task {i+1}: {task.get('action')} | {task.get('ip') or task.get('message') or task.get('details')}")

    # 🔹 2. Executor Agent
    actions_taken = []
    if plan_tasks:
        logger.info("Step 3: Invoking Executor Agent to carry out the plan...")
        actions_taken = await run_executor_agent(plan_output)
        logger.info(f"Executor Agent Completed. Actions recorded: {len(actions_taken)}")
    else:
        logger.info("Step 3: Skipping Executor Agent (no tasks in plan).")
        actions_taken = ["No actions required according to the plan."]

    # 🔹 3. Supervisor Agent
    logger.info("Step 4: Invoking Supervisor Agent for final validation and assessment...")
    supervisor_feedback = await run_supervisor_agent(analysis_results_str, actions_taken)
    logger.info("Supervisor Agent Completed.")
    logger.info(f"Supervisor Assessment: {supervisor_feedback[:100]}...")

    # Add supervisor feedback as a final action or assessment
    actions_taken.append(f"Supervisor Assessment: {supervisor_feedback}")

    logger.info("--- Batch Analysis Workflow Completed Successfully ---")

    return BatchLogResponse(
        overall_risk=overall_risk,
        average_confidence=avg_confidence,
        total_logs=total,
        analysis=results,
        plan=plan_tasks,
        actions_taken=actions_taken
    )

   