from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":"You are an expert in MAths and only and only answer Maths related answer.If query is not related to maths, just say Sorry and do not answer "},
        {"role":"user","content":"Hey, can you solve sin90+cos30"}
    ]
)

print(response.choices[0].message.content)