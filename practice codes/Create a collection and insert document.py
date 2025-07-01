import chromadb
client = chromadb.Client()

collection =client.get_or_create_collection(name='Fruits')

collection.add(
    documents=[
        "Apples are Red",
        "Bananas are yellow",
        "Grapes are green"
    ],
    ids=['1','2','3']
)

print(collection.get())