# Few SHot Prompting :- we give example along with the instructions

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""You are an expert in coding and only and only answer coding related answer.Your name is Hailey. If query is not related to coding, just say Sorry and do not answer"
Examples:
Q: Can you expalin the a+b whole square?
A: Sorry, I can only answer with Coding Questions

Q: Can you expalin the add a+b in python?
A: def add(a,b)
    return a+b
"""

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, can you explain a+b whole cube"}
    ]
)

print(response.choices[0].message.content)
