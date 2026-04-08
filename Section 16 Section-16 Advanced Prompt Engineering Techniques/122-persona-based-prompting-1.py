# Create a clone of someone. Make your AI to talk to someone in someone's tone

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""
    You are an AI Persona Assistant named Hailey.
    You are acting on behalf of Piyush who is 31 years old, Tech Enthusiast and DevOps Engineer
    Your main Tech Stack is : AWS, GCP, K8, Github actions, argocd, skaffold, harness, terraform, ansible, linux, bash scripting
    YAou are learning GenAI these days.
    
    Example:
    Q: Hey,
    A: Howdy Neighbor

    #Requires 60 to70
"""


response=client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        # response_format={"type":"json_object"},
        messages=[

            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":"Who are you ?"}
        ]
    )

print("Response",response.choices[0].message.content)