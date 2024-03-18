"""This function accepts a query text, performs a similarity search to find relevant documents, 
processes the query using a QA chain model, and returns the result obtained from the QA chain model."""

def process_query(query_text, qa_chain, vector_store):
    docs_result = vector_store.similarity_search(query_text)
    result = qa_chain.run(input_documents=docs_result, question=query_text)
    return result
