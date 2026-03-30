from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompts.log_prompt import log_prompt, parser

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

async def analyze_logs(logs: str):
    chain = log_prompt | llm | parser
    response = await chain.ainvoke({"logs": logs})
    return response.dict()