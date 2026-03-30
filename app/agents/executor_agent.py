import json
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.tools.security_tools import block_ip, alert_admin, log_incident

# 🔹 Initialize LLM for Executor
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 Define Tools
tools = [block_ip, alert_admin, log_incident]

# 🔹 Define System Prompt for Executor
executor_system_prompt = """
You are a highly skilled cybersecurity executor. Your goal is to execute the security plan provided to you.

### INSTRUCTIONS:
- You will receive a plan containing several tasks.
- For each task, call the appropriate tool with the correct parameters.
- If a task involves 'block_ip', use the 'block_ip' tool.
- If a task involves 'alert_admin', use the 'alert_admin' tool.
- If a task involves 'log_incident', use the 'log_incident' tool.
- Provide a summary of the actions taken.
"""

# 🔹 Create Agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=executor_system_prompt
)

async def run_executor_agent(plan: dict) -> list[str]:
    """Execute the plan using tools and return results."""
    try:
        plan_str = json.dumps(plan)
        inputs = {"messages": [{"role": "user", "content": f"Execute this plan: {plan_str}"}]}
        
        response = await agent.ainvoke(inputs)
        
        # The agent returns the state dict, which includes the updated messages list
        messages = response.get("messages", [])
        if messages:
            # For simplicity, returning the content of the last message from the agent.
            # In a real tool-calling agent, it might have multiple tool outputs.
            # Let's extract the actual tool outputs or final summary.
            return [messages[-1].content]
        return ["Executor finished without returning a message."]
    except Exception as e:
        return [f"Executor execution error: {str(e)}"]
