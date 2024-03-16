from langchain.chains.question_answering import load_qa_chain

"""This is to simplify the process of loading a QA chain model by providing 
a convenient interface with predefined defaults for the language model and chain type."""

def initialize_qa_chain(llm, chain_type="stuff"):
    return load_qa_chain(llm, chain_type=chain_type)
