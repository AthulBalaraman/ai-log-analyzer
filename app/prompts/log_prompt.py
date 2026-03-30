from langchain_core.prompts import ChatPromptTemplate

log_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a cybersecurity expert."),
    ("human", """
Analyze the logs and return STRICT JSON:

{{
  "summary": "...",
  "suspicious_activity": "...",
  "risk_level": "Low | Medium | High",
  "suggested_action": "..."
}}

Logs:
{logs}
""")
])