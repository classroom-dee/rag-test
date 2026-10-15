#!/bin/bash

docker run -d --name ollama -p 11434:11434 ollama/ollama
docker exec ollama pull nomic-embed-text
docker exec ollama pull llama3.2

docker run -d --name pgvector -p 5432:5432 -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test pgvector/pgvector:pg16
docker exec pgvector psql -U test -d test -c "create extension if not exists vector"

docker run -it -d --name ubuntu ubuntu:noble-lite /bin/bash
