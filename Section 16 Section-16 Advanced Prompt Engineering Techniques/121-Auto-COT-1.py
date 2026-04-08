#Zero  shot prompting :- The model is given direct question or task without prior examples
#FYI: THis was not working with gemini model, but worked with GT
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()

client=OpenAI(
    # api_key="",
    # base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT="""
You are an expert AI assistant in resolving user queries using chain of thought
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be of multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON OUTPUT format
- Only Run 1 step at a time
- the sequence of steps is START (Where user gives an input), PLAN (That can be multiple times ) and finally OUTPUT which is going to be displayed to the user.

OUTPUT JSON FORMAT:
{{
    "step:""START" | "PLAN" | "Output,
    "content" : "string" 
}}

Example:
START: Can you solve 2+3 *5 /10 
PLAN:{{
    "step":"PLAN",
    "content": "Seems like user is interested in MAths PROBLEM"
}}
PLAN:{{
    "step":"PLAN",
    "content": "Looking at the PRoblem,we should solve it using BODMAS method"
}}
PLAN:{{
    "step":"PLAN",
    "content": "BODMAS method is correct to be done here"
}}

PLAN:{{
    "step":"PLAN",
    "content": "Follow each step of BODMAS to reah the single value and iterate the PLAN step for each of the BODMAS STEP applied"
}}
PLAN:{{
    "step":"PLAN",
    "content": "Great, we have solved and finally left with the claculated value"
}}

OUTPUT:{{
    "step":"Output",
    "content": "Output value"
}}
"""

print("\n" * 3)

message_history=[
    {"role":"system","content":SYSTEM_PROMPT},
]

user_query=input("👉")

message_history.append({"role":"user","content":user_query})

while True:
    response=client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        response_format={"type":"json_object"},
        messages=message_history
    )
    raw_result=(response.choices[0].message.content)
    message_history.append({"role":"assistant","content":raw_result})

    parsed_result=json.loads(raw_result)

    if parsed_result.get("step")=="START":
        print(f"Starting LLM Loop:{parsed_result.get("content")}")
        continue
    if parsed_result.get("step")=="PLAN":
        print(f"Planning Process:{parsed_result.get("content")}")
        continue
    if parsed_result.get("step")=="OUTPUT":
        print(f"OUTPUT:{parsed_result.get("content")}")
        break
  