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

# Delete a single document
delete_query = {'name': 'John'}
delete_result = collection.delete_one(delete_query)
print("Number of documents deleted:", delete_result.deleted_count)

# Delete multiple documents
delete_query = {'city': 'New York'}
delete_result = collection.delete_many(delete_query)
print("Number of documents deleted:", delete_result.deleted_count)