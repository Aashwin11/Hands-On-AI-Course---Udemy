from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api=os.getenv("GEMINI_API_KEY")

#adding LLM Model
client=OpenAI(
    api_key=api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Created State
class State(TypedDict):
    messages:Annotated[list,add_messages]
    
    
#Build a state graph
graph_builder=StateGraph(State)


#Creating Nodes
def chat_bot_node(state:State):
    print("\n... Working inside ChatBot Node\n",state)
    input_message=state["messages"][-1].content
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role":"user","content":input_message}
        ]
    )
    return {"messages":[response.choices[0].message.content]}

def end_node(state:State):
    print("\n... Working inside End Node\n",state)
    return {"messages":["\nEnd of the Langgraph\n"]}

#Graph builder does not know that a node is created/existing. We need to explicitly tell that the node exists
graph_builder.add_node("ChatBot-Node",chat_bot_node)
graph_builder.add_node("End-Node",end_node)

#Nodes are ready, we now need to define the EDGES that will connect the nodes
graph_builder.add_edge(START,"ChatBot-Node")
graph_builder.add_edge("ChatBot-Node","End-Node")
graph_builder.add_edge("End-Node",END)


#Compile the graph created
graph=graph_builder.compile()

#to run the graph, we have invoke the graph and pass initial state
updated_state = graph.invoke(State({"messages": ["\nHi, my name is Lisa\n"]}))
print("Updated State:",updated_state)


