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

# Update a single document
update_query = {'name': 'John'}
update_data = {'$set': {'age': 31}}
update_result = collection.update_one(update_query, update_data)
print("Number of documents updated:", update_result.modified_count)