import chromadb
client = chromadb.PersistentClient(
    path="./vectorstore")

collection = client.create_collection (name ="my programming collection")
collection = client.get_collection(name ="my programming collection")

print('collectiion created successfully')