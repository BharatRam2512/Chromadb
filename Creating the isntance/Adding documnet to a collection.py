import chromadb
client = chromadb.PersistentClient(
    path="./vectorstore")
collection=client.get_or_create_collection(name="my_collection")



collection.add(
    documents=[
        "my name is Bharat Ram",
        "I recently completed my B. Tech graduation",
        "I am currently working on a project releated to chromadb",
        "I am learning about chromadb and its features",
        "Chromadb is a very interesting database"
    ],
    metadatas=[
        
        {"source" : "self"},
        {"source": "self"},
        {"source": "self"},
        {"source": "self"},
        {"source": "self"}
    ],
    ids=['1','2','3','4','5']

)

first_ten = collection.peek()
print(first_ten)

collection_count = collection.count()
print(collection_count)
