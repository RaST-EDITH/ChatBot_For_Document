from langchain.chains.question_answering import load_qa_chain
from embedding_utils import create_faiss_database
from document_loader import load_text_document
from langchain import HuggingFaceHub
from question_answering import initialize_qa_chain
import joblib
import os

"""This function takes a query text, performs a similarity search on pre-processed documents using FAISS,
 and then uses a QA chain model to process the query and provide a response or relevant information."""

def train_and_save_model():
    document = load_text_document(os.path.join( os.getcwd(), r"Dataset\data.txt" ))
    db = create_faiss_database(document)

    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.8, "maxlength": 512})
    qa_chain = initialize_qa_chain(llm, chain_type="stuff")

    # Save the model and vector store
    joblib.dump(qa_chain, os.path.join( os.getcwd(), r"Processed_Data\qa_chain_model.joblib" ))
    joblib.dump(db, os.path.join( os.getcwd(), r"Processed_Data\faiss_vector_store.joblib" ))
