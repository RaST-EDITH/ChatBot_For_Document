from langchain.document_loaders import TextLoader

def load_text_document(file_path, encoding="utf-8"):
    loader = TextLoader(file_path, encoding=encoding)
    return loader.load()
