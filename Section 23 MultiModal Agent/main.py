from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

api=os.getenv("GEMINI_API_KEY")
client=OpenAI(
    api_key=api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

prompt=input(">")
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role":"user",
            "content":[
                {"type":"text","text":prompt},
                {"type":"image_url", 
                 "image_url":
                     { 
                      "url":"https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg"
                      }

                }
            ]
        }
    ]
)

print("Response:", response.choices[0].message.content)
