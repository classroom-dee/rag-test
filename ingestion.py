"""
Currently this script is for ad-hoc executions.
"""
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector

print("Downloading text")
res = requests.get("https://www.gutenberg.org/cache/epub/79782/pg79782.txt")

text = res.text

splitter = RecursiveCharacterTextSplitter(
	chunk_size=2000,
	chunk_overlap=200
)

print("Splitting text into chunks")
chunks = splitter.split_text(text)

embeddings = OllamaEmbeddings(
	model="nomic-embed-text",
	base_url="http://host.docker.internal:11434"
)

vec_store = PGVector(
	embeddings = embeddings,
	collection_name = "books",
	connection="postgresql+psycopg://test:test@host.docker.internal:5432/test",
	use_jsonb=True,
)

vec_store.add_texts(chunks)

print(f"Stored chunks: {len(chunks)}")


