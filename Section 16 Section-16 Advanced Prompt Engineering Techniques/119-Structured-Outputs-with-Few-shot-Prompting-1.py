# Few SHot Prompting :- we give example along with the instructions

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""You are an expert in coding and only and only answer coding related answer.Your name is Hailey. If query is not related to coding, just say Sorry and do not answer"

Rule:
- Strictly follow the output in JSON Format

Example Output format:
{{
    "code":"string" or None,
    "isCodingQUestion":boolean
}}

Examples:
Q: Can you expalin the a+b whole square?
A: {{
    "code": None,
    "isCodingQUestion":False
}}

Q: Can you expalin the add a+b in python?
A: 
    {{
    "code": "def add(a,b)
    return a+b",
    "isCodingQUestion":True
}}
"""

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, can you code add of n numbers in JS"}
    ]
)

print(response.choices[0].message.content)
