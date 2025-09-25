from pymongo import MongoClient
from app import initial_activities

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['school_activities']
activities_collection = db['activities']

# Clear existing data
activities_collection.delete_many({})

# Insert initial activities
for name, details in initial_activities.items():
    activities_collection.insert_one({"_id": name, **details})

print("Database initialized successfully!")