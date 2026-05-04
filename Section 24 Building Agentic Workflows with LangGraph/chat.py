from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph


# Created State
class State(TypedDict):
    messages:Annotated[list,add_messages]
    
    
#Build a state graph
graph_builder=StateGraph(State)


#Creating Nodes
def chatbot(state:State):
    return {"messages":["Hi, this is message from ChatBot Node"]}

#Graph builder does not know that a node is created/existing. We need to explicitly tell that the node exists
 