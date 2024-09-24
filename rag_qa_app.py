import os
from langchain import OpenAI, RetrievalQA
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
gemini_api_key = os.getenv('GEMINI_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
embeddings = OpenAIEmbeddings()
# Assuming documents is a list of text documents
vectors = [(doc_id, embeddings.embed(doc)) for doc_id, doc in enumerate(documents)]
vector_index.upsert(vectors)
retriever = Pinecone(vector_index, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(model="gpt-3.5-turbo"),
    chain_type="stuff",
    retriever=retriever
)
def ask_question(question):
    answer = qa({"query": question})
    return answer['result']

if __name__ == "__main__":
    while True:
        user_question = input("Ask your question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break
        response = ask_question(user_question)
        print("Answer:", response)


