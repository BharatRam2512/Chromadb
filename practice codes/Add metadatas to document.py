import chromadb
client = chromadb.Client()

collection =client.get_or_create_collection(name='Fruits')

collection.add(
    documents=[
        "Apples are Red",
        "Bananas are yellow",
        "Grapes are green"
    ],
    ids=['1','2','3'],
    metadatas=[
        {"color": "red", "fruit": "apple"},
        { "fruit": "banana", "color": "yellow"},
        {"color": "green", "fruit": "grapes"}       
    ]
)

for i in range(len(collection.get()['documents'])):
    print("document:", collection.get()['documents'][i], '\t', 'metadatas:', collection.get()['metadatas'][i])