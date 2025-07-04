import chromadb
client=chromadb.PersistentClient(path='./sample')

collection=client.get_or_create_collection(name='animals')

docs=["dog is a faithfull animal",
    "cat is a pet",
    "we can see most of the wild animals in the zoo",
    "most of the metro-politan cities contains luxaries zoos",
    "these zoos contains lots of wild animals of different species"]
       
ids=[]
for i in range(len(docs)):
    ids.append(str(i))

collection.add(
    documents=docs, ids=ids
)
    
search= input("enter a sentence to search:")
results= collection.query(
    query_texts=[search],   
    n_results=1
)

print(results['documents'][0][0])
