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
        {"role":"user",
         "content":"Hey there",
         }
    ]
)

print(response.choices[0].message.content)