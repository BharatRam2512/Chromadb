from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(Settings())

collection = client.get_or_create_collection("custom_embeddings")

documents = ["Python is amazing", "Python is more useful in nowadays", "Tigers are wild animals", "The moon reflects sunlight"]
ids = ["d1", "d2", "d3", "d4"]

embeddings = model.encode(documents).tolist()

collection.add(documents=documents, ids=ids, embeddings=embeddings)

query = input("enter a string to search: ")
query_embedding = model.encode([query]).tolist()

results = collection.query(query_embeddings=query_embedding, n_results=2)
print(results["documents"][0])
