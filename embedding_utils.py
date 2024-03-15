from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

"""Preprocessing the input documents by splitting them into smaller chunks, 
generates embeddings for these chunks, and creates a FAISS database that 
facilitates efficient similarity search operations on the text data"""

def create_faiss_database(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(split_docs, embeddings)
    return db
