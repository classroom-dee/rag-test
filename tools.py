from langchain_core.tools import tool

from rag import init_vector_store, search_vectors


@tool
def retrieve(collection_name: str, question: str):
    """
    Retrieves structured message with the context searched from the vector store.
    List of possible arguments for collection_name: ["books"]
    Args:
        question (str): User's question
        collection_name: Relevant vector collection name to search from
    """
    vector_store = init_vector_store(collection_name)
    context = search_vectors(vector_store, question, k=5)
    # message = get_structured_message(context, question)
    # return message
    return context


tools_list = [retrieve]
