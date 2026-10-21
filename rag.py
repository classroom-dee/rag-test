"""
It needs modularizing on expansion, if ever.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_postgres import PGVector


def init_llm():
    return ChatOllama(
        model="llama3.2",
        base_url="http://host.docker.internal:11434",
    )


def init_vector_store(collection_name: str):
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text", base_url="http://host.docker.internal:11434"
    )

    vec_store = PGVector(
        embeddings=embeddings,
        collection_name=collection_name,
        connection="postgresql+psycopg://test:test@host.docker.internal:5432/test",
        use_jsonb=True,
    )

    return vec_store


def search_vectors(vector_store, question, k=5):
    docs = vector_store.similarity_search(question, k)
    # context
    return "\n\n".join(doc.page_content for doc in docs)


def get_structured_message(context, question):
    prompt = ChatPromptTemplate.from_template("""
		Answer the question using only the context below.
		If the answer is not in the context, say you don't know.
		
		Context:
		{context}
	
		Question:
		{question}
	""")

    return prompt.format_messages(context=context, question=question)
