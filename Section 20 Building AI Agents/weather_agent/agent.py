from openai import OpenAI
import requests, json, time, os, subprocess, shutil
from dotenv import dotenv_values
from pydantic import BaseModel,Field
from typing import Optional     


#Tools
BASH_PATH = shutil.which("bash") or r"C:\Program Files\Git\bin\bash.exe"
def run_command(cmd:str):
    result = subprocess.run([BASH_PATH, "-c", cmd], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr

def get_weather(city: str):
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return (f"The weather of {city} is: {response.text}")
    return (f"Something went wrong {response.status_code}")


class MyOutputFormat(BaseModel):
    step: str=Field(..., description="The ID of the step")
    content: Optional[str]=Field(None, description="Optional string")
    tool: Optional[str]=Field(None, description="Id of the tool to call")
    input: Optional[str]=Field(None, description="Input params for the tool")

    
    
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
- When modifying files, prefer overwriting the entire file with the new content rather than using complex regex like sed, unless specifically asked to edit a single line
- Create a new file if needed when prompted by user

AVAILABLE TOOLS:
- get weather
- run_command(cmd:str) : Takes a system Linux command as a string and executes the command on user's system and returns the output from that command.

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
OUTPUT: {"step":"PLAN","content":"✅:Tool get_weather executed"}
PLAN :  {"step":"PLAN","content":"🤖:Generating User Output"}
OUTPUT: {"step":"OUTPUT","content":"✅:Greetings Aashwin, The Weather for the Delhi is 20 C. Looks partially cloudy. Carry an Umbrella "}
"""

user_input=input("> ")
messages=[{"role":"system","content":SYSTEM_PROMPT,},
    {"role":"user","content":user_input},
    ]
while True:
    time.sleep(10)
    response=client.chat.completions.parse(
    model="gemini-2.5-flash-lite",
    messages=messages,
    response_format=MyOutputFormat
    )
    messages.append({"role":"assistant","content":response.choices[0].message.content})
    parsed_result=response.choices[0].message.parsed
    
    if parsed_result.step=="START":
        print(f"{parsed_result.input}")
        continue
    if parsed_result.step=="PLAN":
        print(f"{parsed_result.content}")
        continue
    if parsed_result.step=="TOOL":
        tool_name=parsed_result.tool
        tool_input=parsed_result.input
        
        if tool_name=="get_weather":
            print(f"Executing tool {tool_name} for {tool_input}...")
            tool_response=get_weather(tool_input)
        elif tool_name == "run_command":
            print(f"Executing system command: {tool_input}")
            tool_response = run_command(tool_input)
        else:
            tool_response=f"Tool {tool_name} is not found"
        messages.append(
            {"role":"user","content":f"Observation:{tool_response}"},

        )
        
        continue
    
    if parsed_result.step=="OUTPUT":
        print(f"FINAL OUTPUT:{parsed_result.content}")
        break
    

