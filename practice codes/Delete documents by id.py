import chromadb
client=chromadb.Client()

collection=client.get_or_create_collection(name='My_collection')

collection.add(
    documents = ["Python is amazing", "Python is more useful in nowadays", "Tigers are wild animals", "The moon reflects sunlight"],
    ids = ["d1", "d2", "d3", "d4"]
)

collection.delete(ids=['d2'])

print(collection.get())