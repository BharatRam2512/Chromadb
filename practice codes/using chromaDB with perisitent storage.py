import chromadb
client=chromadb.PersistentClient(
    path="./sample_codes"
)

collection = client.get_or_create_collection(name='animals')

collection.add(
    documents=[
        'cats are independent animals', 
        'dogs are loyal and faithful pets'
    ],
    metadatas=[
        {"source": "self"},
        {"source": "self"}
    ],
    ids=['s1','s2']
)
print(collection.get())