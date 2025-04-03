import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the translated transcript
def load_translated_transcript(filename="translated.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Convert transcript into text chunks
def get_text_chunks(transcript):
    return [segment["text"] for segment in transcript]

#sentence embedding model (FAISS)
def create_faiss_index(text_chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2") 
    embeddings = model.encode(text_chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings, dtype=np.float32))
    
    return index, text_chunks, model

#search for the most relevant text chunk
def retrieve_answer(query, index, text_chunks, model):
    query_embedding = model.encode([query])
    _, indices = index.search(np.array(query_embedding, dtype=np.float32), k=1)  
    
    return text_chunks[indices[0][0]]

def chatbot():
    transcript = load_translated_transcript()
    text_chunks = get_text_chunks(transcript)
    index, text_chunks, model = create_faiss_index(text_chunks)

    print("\nAsk any question about the translated transcript.")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting chatbot. Goodbye!")
            break
        answer = retrieve_answer(query, index, text_chunks, model)
        print("Bot:", answer)

if __name__ == "__main__":
    chatbot()