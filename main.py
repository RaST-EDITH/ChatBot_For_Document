from config import *
from document_loader import load_text_document
from text_utils import wrap_text_preserve_newlines
from embedding_utils import create_faiss_database
from question_answering import initialize_qa_chain
from model_training import train_and_save_model
from query_processor import process_query
import joblib
import os

""" This function provides a high-level interface for training or loading a model and vector store, 
processing a query using the loaded model and vector store, and displaying the result."""

# Check if the model and vector store are already trained and saved
if not os.path.isfile(os.path.join( os.getcwd(), r"Processed_Data\qa_chain_model.joblib" )) or not os.path.isfile(os.path.join( os.getcwd(), r"Processed_Data\faiss_vector_store.joblib" )):
    print("Training the model for the first time...")
    train_and_save_model()

# Load the model and vector store
qa_chain = joblib.load(os.path.join( os.getcwd(), r"Processed_Data\qa_chain_model.joblib" ))
vector_store = joblib.load(os.path.join( os.getcwd(), r"Processed_Data\faiss_vector_store.joblib" ))

# Query
query_text = "SRK win how many awards and prizes in his career"
result = process_query(query_text, qa_chain, vector_store)

# Display Result
print(result)
