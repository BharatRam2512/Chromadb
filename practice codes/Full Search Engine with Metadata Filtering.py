import chromadb
client=chromadb.Client()

collection=client.get_or_create_collection(name='my_collection')

collection.add(
    documents=['Python is an open source programaming languages',
               'java and python are oop languages',
               'c is the fundamental programmming languages'],
    ids=['id1','id2','id3'],
    metadatas=[
        {'topic':'programming language'},
        {'topic':'programming language'},
        {'topic':'programming language'}
    ]
)


# query="tell me about programming languages"
results= collection.query(
    query_texts="tell me about languages",
    n_results=3,
    where={'topic':'programming language'}
)

for i in results['documents'][0]:
    print(i)
print(results['distances'][0])