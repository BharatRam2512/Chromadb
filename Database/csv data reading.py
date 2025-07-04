import pandas as pd
import chromadb

client= chromadb.PersistentClient(path="./sample_codes")

collection=client.get_or_create_collection(name='student_marks')


df = pd.read_csv(r'C:\Users\bhara\OneDrive\Desktop\Folders\ML Projects\Chromadb\Database\data.csv', on_bad_lines='skip')

collection.add(
    documents=[str(row) for _, row in df.iterrows()],
    ids=[str(i) for i in df.index]

)


print(collection.get(['documents']))