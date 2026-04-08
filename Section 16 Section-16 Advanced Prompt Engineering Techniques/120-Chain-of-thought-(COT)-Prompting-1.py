#Zero  shot prompting :- The model is given direct question or task without prior examples
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#zero shot prompting- Directly giving the instruction to the model

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
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, write a code for adding n numbers in JS "},
        #Manually keep appending message to the history
        {"role":"assistant","content":json.dumps({
    "step": "START",
    "content": "User wants a JavaScript function to add 'n' numbers."
})},
{"role":"assistant","content":json.dumps({
    "step": "PLAN",
    "content": "The user is asking for a JavaScript function to add 'n' numbers. I should define a function that can accept multiple arguments."
})},

{"role":"assistant","content":json.dumps({
    "step": "PLAN",
    "content": "A common way to handle 'n' numbers in JavaScript is using the rest parameter (...) in the function definition, which collects all arguments into an array."
})},
{"role":"assistant","content":json.dumps({
    "step": "PLAN",
    "content": "Inside the function, I'll need to iterate through the array of numbers and sum them up. A `forEach` loop or `reduce` method would be suitable."
})}


    ]
)

print(response.choices[0].message.content)
