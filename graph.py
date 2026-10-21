from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from rag import init_llm
from tools import tools_list

llm = init_llm().bind_tools(tools_list)


def chat_node(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


workflow = StateGraph(MessagesState)

workflow.add_node("chat_node", chat_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "chat_node")
workflow.add_conditional_edges("chat_node", tools_condition)
workflow.add_edge("tools", "chat_node")

graph = workflow.compile()
