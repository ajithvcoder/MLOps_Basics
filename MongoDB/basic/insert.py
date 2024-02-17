from pymongo import MongoClient

# Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Assuming MongoDB is running locally on default port

client = MongoClient(host='mongodb_connect',
                        port=27017, 
                        username='root', 
                        password='pass',
                    authSource="admin")
db = client['mydatabase']
print("connected with db")


# Access a collection
collection = db['mycollection']

# Insert a single document
data = {'name': 'John', 'age': 30, 'city': 'New York'}
inserted_document = collection.insert_one(data)
print("Inserted document ID:", inserted_document.inserted_id)

# Insert multiple documents
data_list = [
    {'name': 'Alice', 'age': 25, 'city': 'London'},
    {'name': 'Bob', 'age': 35, 'city': 'Paris'}
]
inserted_documents = collection.insert_many(data_list)
print("Inserted documents IDs:", inserted_documents.inserted_ids)





