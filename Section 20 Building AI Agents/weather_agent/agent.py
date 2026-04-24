from openai import OpenAI
import requests, json
from dotenv import dotenv_values
def get_weather(city: str):
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return (f"The weather of {city} is: {response.text}")
    return (f"Something went wrong {response.status_code}")


#Creating Client
client = OpenAI(
    api_key=dotenv_values(".env")["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#SYSTEM_PROMPT
SYSTEM_PROMPT="""
You are an AI Agent Who is trained to perform The actions required by the user User Gives input And you need to Act On User will Ask a question based on the entire Question you need to act Think use the tools that are given to you And then answer the user Its question.

Rules:
- You must only output EXACTLY ONE JSON object per turn. Do not output a list of steps
- Always rely on using the Tools given to you for usage
- Strictly understand the user's input and REACT accordingly
- Think and act for each step.
- Do not allow the pre trained model to overwrite your thoughts until needed.

AVAILABLE TOOLS:
- get weather

OUTPUT JSON FORMAT:
{
    "step":"START or PLAN or TOOL or OUTPUT",
    "content":"string",
    "tool":"string",
    "input":"string",
} 


EXAMPLE:
START: {"step":"START","input":"👤:CAn you tell me the weather of Delhi"}
PLAN : {"step":"PLAN","input":"🤖:User gave city intersted in"}
PLAN : {"step":"PLAN","content":"🤖:User is interested to know the weather about Delhi"}
PLAN :  {"step":"PLAN","content":"🤖:Looking for available Tools"}
PLAN :  {"step":"PLAN","content":"✅:Found Tool get_weather"}
TOOL :  {"step":"TOOL","tool":"get_weather"}
OUTPUT: {"step":"OUTPUT","content":"✅:Tool get_weather executed"}
PLAN :  {"step":"PLAN","content":"🤖:Generating User Output"}
OUTPUT: {"step":"OUTPUT","content":"✅:Greetings Aashwin, The Weather for the Delhi is 20 C. Looks partially cloudy. Carry an Umbrella "}
"""

user_input=input("> ")
messages=[{"role":"system","content":SYSTEM_PROMPT,},
    {"role":"user","content":user_input},
    ]
while True:
    response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages,
    response_format={"type":"json_object"}
    )
    messages.append({"role":"assistant","content":response.choices[0].message.content})
    parsed_result=json.loads(response.choices[0].message.content)
    
    if parsed_result["step"]=="START":
        print(f"{parsed_result['input']}")
        continue
    if parsed_result["step"]=="PLAN":
        print(f"{parsed_result['content']}")
        continue
    if parsed_result["step"]=="TOOL":
        tool_name=parsed_result['tool']
        tool_input=parsed_result.get('input','Delhi')
        
        if tool_name=="get_weather":
            print(f"Executing tool {tool_name} for {tool_input}...")
            tool_response=get_weather(tool_input)
        else:
            tool_response=f"Tool {tool_name} is not found"
        messages.append(
            {"role":"user","content":f"Observation:{tool_response}"},

        )
        
        continue
    
    if parsed_result["step"]=="OUTPUT":
        print(f"FINAL OUTPUT:{parsed_result['content']}")
        break
    

