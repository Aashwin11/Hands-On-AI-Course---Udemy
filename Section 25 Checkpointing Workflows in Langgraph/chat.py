from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.checkpoint.mongodb import MongoDBSaver  
import os


load_dotenv()
api=os.getenv("GEMINI_API_KEY")

#adding LLM Model
llm=ChatOpenAI(
    model="gemini-2.5-flash",
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
    print("\n... Working inside ChatBot Node\n")
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def end_node(state:State):
    print("\n... Working inside End Node\n")
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

# in the complie we can create function to complie grapgh with checkpointer

def compile_graph_with_checkpointer(checkpointer):
    graph=graph_builder.compile(checkpointer=checkpointer)
    return graph


MONGODB_URI='mongodb://admin:admin@localhost:27017'
with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
    graph_with_checkpointer=compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
            "configurable": {
                "thread_id": "John"
            }
        }


    #to run the graph, we have invoke the graph and pass initial state
    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["\nWhat is my name ?\n"]}),
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()


