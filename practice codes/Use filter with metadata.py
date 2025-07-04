import chromadb
client=chromadb.Client()

collection = client.get_or_create_collection (name='Fruits')

collection.add(
    documents=[
        "lemons are sour",
        "limes are small green citrus fruits"
    ],
    ids=['senteence1', 'sentence 2'],
    metadatas=[
        {'type' : 'citrus', 'fruit' : 'lemon'},
        {'type' : 'citrus', 'fruit' : 'lime'}
    ]
)
results=collection.query(
    query_texts=['what is citrus fruit'], 
    n_results=2, 
    where={'type' : 'citrus'}
)

print(results['documents'][0])