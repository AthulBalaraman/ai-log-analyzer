from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.schemas.log_schema import LogResponse

parser = PydanticOutputParser(pydantic_object=LogResponse)

log_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a cybersecurity expert."),
    ("human", """
Analyze the logs and return structured JSON.

{format_instructions}

Logs:
{logs}
""")
]).partial(format_instructions=parser.get_format_instructions())
