from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.schemas.log_schema import LogResponse

parser = PydanticOutputParser(pydantic_object=LogResponse)

log_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an advanced cybersecurity analyst.

Your job:
1. Identify log type
2. Detect attack patterns
3. Assess risk intelligently
"""),

    ("human", """
Analyze the logs and return structured JSON.

Definitions:
- log_type: authentication | api | database | network | system
- attack_type: brute_force | sql_injection | ddos | none | unknown
- confidence_score: 0 to 100

{format_instructions}

Logs:
{logs}
""")
]).partial(format_instructions=parser.get_format_instructions())