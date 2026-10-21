from fastapi.routing import APIRouter

from graph import graph

router = APIRouter(prefix="/chat", tags=["chat"])


@router.get("")
def chat(message):
    result = graph.invoke({"messages": [("user", message)]})

    return result["messages"][-1].content
