from .rag import init, search_vectors, get_structured_message

question = "THIS NEEDS TO COME FROM REQUESTS"
vector_store, llm = init("books")
context = search_vectors(vector_store, question, k=5)
message = get_structured_message(context, question)

# define a node that uses rag.py's invoke function
def chat_node(state):
	llm.invoke()
# build graph that includes the node

# fastapi post api with message parameter

# invoke the graph inside the api

# return response
