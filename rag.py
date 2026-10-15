from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_postgres import PGVector
from langchain_core.prompts import ChatPromptTemplate


def init(collection_name: str):
	embeddings = OllamaEmbeddings(
		model="nomic-embed-text",
		base_url="http://host.docker.internal:11434"
	)

	vec_store = PGVector(
		embeddings=embeddings,
		collection_name=collection_name,
		connection="postgresql+psycopg://test:test@host.docker.internal:5432/test",
		use_jsonb=True,
	)

	llm = ChatOllama(
		model="llama3.2",
		base_url="http://host.docker.internal:11434",
	)
	return vec_store, llm

def search_vectors(vector_store, question, k=5):
	docs = vector_store.similarity_search(question, k=5)
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
	
	return prompt.format_messages(
		context=context,
		question=question
	)


res = llm.invoke(message)

print(res.content)
