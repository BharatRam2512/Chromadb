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
    ])

results=collection.query(
    query_texts=["what is the color of apple"],
    n_results=1
)
print(results['documents'][0])


