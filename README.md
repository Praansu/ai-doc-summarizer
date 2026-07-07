# AI Doc Summarizer

A simple RAG-based app that lets you upload a PDF and ask questions about it. Built to understand how retrieval-augmented generation works.

## What it does

Upload any PDF document, type a question, and the app finds the most relevant parts of the document to answer. Uses vector search to figure out what parts of the document match your question.

## How I built it

- Loaded the PDF and split it into chunks of text
- Created embeddings (vector representations) of each chunk using OpenAI
- Stored them in ChromaDB so it can search through them fast
- When a question is asked, it finds the most similar chunks and sends them to GPT-4o-mini along with the question

## Run it yourself

```
pip install -r requirements.txt
streamlit run app.py
```

You need an OpenAI API key. You can either put it in a .env file as OPENAI_API_KEY or type it in the sidebar when the app opens.

## What I learned

- How RAG actually works under the hood (not just the theory)
- Using LangChain to chain together document loading, splitting, embedding, and QA
- ChromaDB for vector storage and similarity search
- Building a simple Streamlit UI that feels okay to use

## Stack

LangChain, ChromaDB, OpenAI, Streamlit
