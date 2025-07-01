import chromadb
client=chromadb.Client()

collection=client.create_collection(name='student_names')
names=['Murali Krishna',
       'Vasanth kumar',
       'Jahangeer Naidu',
       'Manikanta',
       'Rakshitha',
       'Kavya sree',
       'Pavani devi',
       'Likhith Naidu',
       'Umesh Chandra Sai',
       'Vasavi',
       'Sai Sakeeth',
       'Thanuja',
       'Jahnavi',
       'Bharat Ram',
       'Sai Srujana',
       'Hima Bindu',
       'Dilleswara Rao',
       'Rohith Kumar',
       'Khyama Mahanty',
       'Vijay','Dinesh',
       'Hari Krishna',
       'Jaya Sree',
       'Likhitha',
       'Nikitha',
       'Jyothi',
       'Prudhvi Krishna',
       'Dinesh pekala',
       'Karthik',
       'Siva Krishna',
       'Somesh']

collection.add(
    documents=names,
    ids=[str(i) for i in range(len(names))]
)
print("Collection created and names added successfully.")

def similar_search(search_name, top_k):
    result=collection.query(
        query_texts=[search_name],
        n_results=top_k
    )
    return result['documents'][0]

search_name=input("Enter a name to search: ")
top_k=int(input("Enter the number of similar names to retrieve: "))

similar=similar_search(search_name, top_k)

print("similar names are: ")


for i in similar:
    print(i)
