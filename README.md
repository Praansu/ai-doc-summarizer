# AI Doc Summarizer

Upload a PDF, ask questions about it, get answers. It's RAG (retrieval-augmented generation) in its simplest form — built because I wanted to understand how "chat with your PDF" apps actually work under the hood.

## How it works (in plain English)

1. You upload a PDF. The app splits it into chunks (paragraph-sized pieces).
2. Each chunk gets converted to a vector embedding (a numerical representation of its meaning) using OpenAI.
3. Those embeddings live in ChromaDB — a vector database that can quickly find similar content.
4. When you ask a question, it finds the chunks most relevant to your question and sends them to GPT-4o-mini along with the question.
5. GPT reads the relevant chunks and gives you an answer based on the document, not its training data.

Still amazed this actually works.

## Running it

```bash
pip install -r requirements.txt
streamlit run app.py
```

You'll need an OpenAI API key. Drop it in a `.env` file as `OPENAI_API_KEY` or type it in the sidebar when the app opens.

## What I figured out

- LangChain makes the "chain" concept click once you actually use it
- Chunk size matters — too big and you lose context, too small and you miss connections
- ChromaDB is surprisingly easy to set up for local vector search
- RAG is elegant: it solves the "LLM doesn't know about your data" problem without fine-tuning

## Stack

LangChain, ChromaDB, OpenAI, Streamlit

## License

MIT
