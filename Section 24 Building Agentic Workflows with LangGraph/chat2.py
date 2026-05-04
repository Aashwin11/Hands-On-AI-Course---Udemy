import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from openai import OpenAI
from langgraph.graph import StateGraph, START, END



load_dotenv()
api=os.getenv("GEMINI_API_KEY")

#adding LLM Model
client=OpenAI(
    api_key=api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class State(TypedDict):
    user_query:str
    llm_output:Optional[str]
    is_good:Optional[bool]
    
graph_builder=StateGraph(State)

def chatbot_node(state:State):
    
    print("\n\n Inside gemini-2.5-flash Chatbot Node")
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{
            "role":"user",
            "content":state.get("user_query")  
        }
        ]
    )
    
    state["llm_output"]=response.choices[0].message.content
    return state

def evaluation_node(state:State) -> Literal["chatbot-3","end-node"]:
    
    print("\n\n Entered Evaluation Node")
    if False:
        return "end-node"
    else:
        return "chatbot-3"
    
    
def chatbot_node2(state:State):
    
    print("\n\n Inside gemini-3.1-flash-lite-preview Chatbot Node")
    response=client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[{
            "role":"user",
            "content":state.get("user_query")  
        }
        ]
    )
    
    state["llm_output"]=response.choices[0].message.content
    return state

def end_node(state:State):
    print("\n\n  Entered End Node")
    return state


graph_builder.add_node("chatbot-2.5",chatbot_node)
graph_builder.add_node("chatbot-3",chatbot_node2)
graph_builder.add_node("end-node",end_node)



graph_builder.add_edge(START,"chatbot-2.5")
graph_builder.add_conditional_edges("chatbot-2.5",evaluation_node)
graph_builder.add_edge("chatbot-3","end-node")
graph_builder.add_edge("end-node",END)


graph=graph_builder.compile()

updated_state=graph.invoke(State({"user_query":"What is 2*2"}))
print("\n\n Updated State",updated_state)