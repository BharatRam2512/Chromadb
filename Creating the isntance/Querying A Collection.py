import chromadb
client = chromadb.PersistentClient(
    path="./vectorstore")

collection = client.get_or_create_collection (name="my_collection")
print(collection.get())
result=collection.query(
    query_texts =["learning"],
    n_results=4

)
result=collection.query(
    query_texts =["my name is Bharat Ram"],
    n_results=4
    
)

print(result)