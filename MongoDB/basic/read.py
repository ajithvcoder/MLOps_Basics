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
# Query the collection
query = {'city': 'New York'}
results = collection.find(query)

# Print the results
print("Query Results:")
for result in results:
    print(result)