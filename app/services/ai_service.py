import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompts.log_prompt import log_prompt, parser
from app.schemas.log_schema import BatchLogResponse, LogResponse
from app.tools.security_tools import block_ip, alert_admin, log_incident
from app.utils.ip_extractor import extract_ip

# 🔹 Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 Analyze a single log with fallback
async def analyze_single_log(chain, log: str) -> LogResponse:
    try:
        response = await chain.ainvoke({"logs": log})
        return response  # already a LogResponse (due to parser)

    except Exception as e:
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
    chain = log_prompt | llm | parser

    # 🔥 Run all logs in parallel
    tasks = [analyze_single_log(chain, log) for log in logs]
    results = await asyncio.gather(*tasks)

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
    actions_taken = await take_actions(results, logs)
    return BatchLogResponse(
        overall_risk=overall_risk,
        average_confidence=avg_confidence,
        total_logs=total,
        analysis=results,
        actions_taken=actions_taken
    )

async def take_actions(results, logs):
    actions = []

    for result, log in zip(results, logs):
        ip = extract_ip(log)

        # 🔴 HIGH RISK → Full action
        if result.risk_level == "High":
            actions.extend([
                block_ip.invoke({"ip": ip}),
                alert_admin.invoke({"message": result.summary}),
                log_incident.invoke({"details": result.suspicious_activity})
            ])

        # 🟡 MEDIUM RISK → Alert + Log
        elif result.risk_level == "Medium":
            actions.extend([
                alert_admin.invoke({"message": result.summary}),
                log_incident.invoke({"details": result.suspicious_activity})
            ])

        # 🟢 LOW RISK → Only log
        else:
            actions.append(
                log_incident.invoke({"details": result.suspicious_activity})
            )

    return actions

   