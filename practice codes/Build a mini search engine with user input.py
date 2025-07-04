import chromadb
client=chromadb.PersistentClient(path='./sample')

collection=client.get_or_create_collection(name='animals')


docs=["dog is a faithfull animal",
            "cat is a pet",
            "we can see most of the wild animals in the zoo",
            "most of the metro-politan cities contains luxaries zoos",
            "these zoo contains lots of "]

ids=[]
for i in range(len(docs)):
    ids.append(str(i+1))

collection.add()