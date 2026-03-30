import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# 🔹 Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 System Prompt for Planner
planner_system_prompt = """
You are a highly skilled cybersecurity planner. Your goal is to analyze security log analysis results and create a structured plan of action.

### ANALYSIS GUIDELINES:
1. **High Risk (e.g., brute_force, sql_injection, ddos):**
   - Plan to block the IP address if it is clearly provided in the logs.
   - Plan to alert the administrator with specific details.
   - Plan to log the incident.

2. **Medium Risk:**
   - Plan to alert the administrator.
   - Plan to log the incident.

3. **Low Risk / No Threat:**
   - Plan to log the incident for auditing purposes only.

### OUTPUT FORMAT:
You MUST return ONLY a JSON object with the following structure:
{{
  "tasks": [
    {{"action": "block_ip", "ip": "..."}},
    {{"action": "alert_admin", "message": "..."}},
    {{"action": "log_incident", "details": "..."}}
  ]
}}

### INSTRUCTIONS:
- Be strict about JSON output. No other text.
- Decide which actions are needed based on the risk levels and attack types.
- Extract IPs from logs if necessary for 'block_ip' action.
"""

async def run_planner_agent(analysis_results: str) -> dict:
    """Analyze results and return a structured JSON plan."""
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", planner_system_prompt),
            ("human", "Analyze these results and provide a plan: {results}")
        ])
        
        chain = prompt | llm
        
        response = await chain.ainvoke({"results": analysis_results})
        
        # Parse JSON
        plan_text = response.content.strip()
        if plan_text.startswith("```json"):
            plan_text = plan_text[7:-3].strip()
        elif plan_text.startswith("```"):
            plan_text = plan_text[3:-3].strip()
            
        plan = json.loads(plan_text)
        return plan
    except Exception as e:
        print(f"Planner error: {str(e)}")
        return {"tasks": []}
