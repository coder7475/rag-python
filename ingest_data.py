from get_embeddings import get_embedding
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pymongo import MongoClient
from app.config import settings


async def ingest_data():
    # Load the PDF
    loader = PyPDFLoader(
        "https://drive.google.com/file/d/1JGkZkTcG_OC6XPCZQ0AWW5Nfa0chkP0a/view?usp=sharing"
    )
    data = loader.load()

    # Split the data into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=20)
    documents = text_splitter.split_documents(data)

    # Prepare documents for insertion
    docs_to_insert = [
        {"text": doc.page_content, "embedding": get_embedding(doc.page_content)}
        for doc in documents
    ]

    # Connect to your Atlas cluster
    client = MongoClient(settings.atlas_connection_string)
    collection = client["rag-atlas"]["starter"]

    # Insert documents into the collection
    result = collection.insert_many(docs_to_insert)
