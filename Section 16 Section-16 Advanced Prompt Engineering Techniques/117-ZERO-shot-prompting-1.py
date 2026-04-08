#Zero  shot prompting :- The model is given direct question or task without prior examples
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#zero shot prompting- Directly giving the instruction to the model

SYSTEM_PROMPT="You are an expert in coding and only and only answer coding related answer.Your name is Hailey. If query is not related to coding, just say Sorry and do not answer "

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hey, can you write me a code to tell the time in America now"}
    ]
)

print(response.choices[0].message.content)
