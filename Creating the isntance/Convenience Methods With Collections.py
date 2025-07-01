import chromadb
client = chromadb.PersistentClient(
    path="./vectorstore")

#we can do creaating or getting of collection in a single line
collection= client.get_or_create_collection(name='my_collections')

#get a list of first 10 items
first_ten=collection.peek()
print(first_ten)

#get a count of all items in the colection
collection_count =collection.count()
print(collection_count)

