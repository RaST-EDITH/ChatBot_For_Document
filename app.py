import os
from dotenv import load_dotenv
import textwrap
from langchain import HuggingFaceHub
# from langchain_community.llms import HuggingFaceHub
from langchain.vectorstores import FAISS
# from langchain_community.vectorstores import FAISS
from langchain.document_loaders import TextLoader
# from langchain_community.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"]=os.getenv("HUGGINGFACEHUB_API_TOKEN")
loader = TextLoader("data.txt", encoding = "utf-8")
document = loader.load()

def wrap_text_preserve_newlines( text, width=110 ) :
    lines = text.split('\n')
    wrapped_lines = [ textwrap.fill( line, width=width) for line in lines ]
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

text_splitter = CharacterTextSplitter( chunk_size=1500, chunk_overlap=0)
docs = text_splitter.split_documents(document)

embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# query = "SRK net worth?"
# doc = db.similarity_search(query)

# print(wrap_text_preserve_newlines(str(doc[0].page_content)))
llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.8, "maxlength":512})
chain = load_qa_chain(llm, chain_type="stuff")

queryText = "SRK son, daughter, wife name?"
docsResult = db.similarity_search(queryText)
# print(chain.invoke(input_documents = docsResult, question = queryText))
print(chain.run(input_documents = docsResult, question = queryText))
