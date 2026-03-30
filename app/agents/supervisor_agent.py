from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# 🔹 Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 🔹 System Prompt for Supervisor
supervisor_system_prompt = """
You are a senior cybersecurity supervisor. Your goal is to review and validate the results of the log analysis and the actions taken by the executor agent.

### RESPONSIBILITY:
1. **Validate results:** Ensure the final outcome is accurate and logical based on the provided logs and analysis.
2. **Ensure no unnecessary actions:** Check if the executor performed unnecessary actions (e.g., blocking an IP for a low-risk event).
3. **Refine summary:** Provide a final, polished summary of the analysis and actions taken.

### INSTRUCTIONS:
- Review the analysis results and the list of actions taken by the executor.
- If you find any unnecessary actions or discrepancies, mention them in your summary.
- Provide a clear final assessment of the security situation.
"""

async def run_supervisor_agent(analysis_results: str, actions_taken: list[str]) -> str:
    """Validate results and refine the summary."""
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", supervisor_system_prompt),
            ("human", "Analysis Results: {results}\nActions Taken: {actions}\nProvide your final assessment.")
        ])
        
        chain = prompt | llm
        
        response = await chain.ainvoke({
            "results": analysis_results,
            "actions": ", ".join(actions_taken)
        })
        
        return response.content
    except Exception as e:
        print(f"Supervisor error: {str(e)}")
        return "Supervisor failed to validate actions."
