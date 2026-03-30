from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tools.security_tools import block_ip, alert_admin, log_incident

# 🔹 Initialize LLM for Agent
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 Define Tools
tools = [block_ip, alert_admin, log_incident]

# 🔹 Define System Prompt
system_prompt = """
You are a highly skilled cybersecurity expert. Your mission is to analyze security log analysis results and take appropriate actions using the provided tools.

### ACTION GUIDELINES:
1. **High Risk (e.g., brute_force, sql_injection, ddos):**
   - Block the IP address if provided.
   - Alert the administrator.
   - Log the incident with full details.

2. **Medium Risk:**
   - Alert the administrator.
   - Log the incident.

3. **Low Risk / No Threat:**
   - Only log the incident for auditing purposes.

### INSTRUCTIONS:
- Only use tools when necessary based on the risk level.
- Be precise and do not perform unnecessary actions.
- Provide a clear summary of what you did.
"""

# 🔹 Create Agent
# In langchain v1.2+, create_agent returns a compiled LangGraph StateGraph directly.
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

async def run_security_agent(analysis_results: str) -> str:
    """Run the agent on log analysis data."""
    try:
        inputs = {"messages": [{"role": "user", "content": analysis_results}]}
        response = await agent.ainvoke(inputs)
        # The agent returns the state dict, which includes the updated messages list
        messages = response.get("messages", [])
        if messages:
            return messages[-1].content
        return "Agent finished without returning a message."
    except Exception as e:
        return f"Agent execution error: {str(e)}"
