from get_embeddings import get_embedding
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pymongo import MongoClient

# Load the PDF
loader = PyPDFLoader("https://investors.mongodb.com/node/12236/pdf")
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
client = MongoClient(
    "mongodb+srv://rag:V0oyZYxieV05mPKL@cluster0.xjslrno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
collection = client["rag_db"]["test"]

# Insert documents into the collection
result = collection.insert_many(docs_to_insert)
