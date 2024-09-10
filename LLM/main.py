import os
from dotenv import load_dotenv
from Services.bookServices import find_books
from LLM.helper_functions import *
import json

load_dotenv()
os.environ['OPENAI_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


def encode_json(chunk_size=1000):
    books = find_books()
    documents = json.loads(books)
    text_splitter = RecursiveJsonSplitter(
        max_chunk_size=chunk_size
    )
    texts = text_splitter.create_documents(texts=documents, convert_lists=True)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore


def query_retriever():
    chunks_vector_store = encode_json(chunk_size=1000)
    chunks_query_retriever = chunks_vector_store.as_retriever(search_kwargs={'k': 2})
    return chunks_query_retriever


def get_question_answer(question):
    test_query = question
    context = retrieve_context_per_question(test_query, query_retriever())
    return context
