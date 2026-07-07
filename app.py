import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="SmartContent AI", layout="wide")
st.title("📄 SmartContent: AI Document QA")

# Sidebar for API Key if not in .env
with st.sidebar:
    openai_key = st.text_input("OpenAI API Key", type="password")
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and "openai_api_key" in os.environ:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    # 1. Load and Split Document
    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 2. Create Vector Store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # 3. Setup QA Chain
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())

    query = st.text_input("Ask a question about your document:")
    if query:
        with st.spinner("Analyzing..."):
            response = qa_chain.invoke(query)
            st.markdown(f"### Answer:\n{response['result']}")
elif not uploaded_file:
    st.info("Please upload a PDF document to begin.")
else:
    st.error("Please provide an OpenAI API Key in the sidebar.")
