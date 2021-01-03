import os
import pymongo
if os.path.exists("env.py"):
    import env

# python constants
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myTestDB"
COLLECTION = "myFirstMDB"


# function to connect our mongo database
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e


# call connection function and pass hidden env variable MONGO_URI
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]


new_doc = {
    "first": "douglas", "last": "adams", "dob": "11/03/1952",
    "hair_colour": "grey", "occupation": "writer", "nationality": "british"}

coll.update_one({"nationality": "american"}, {"$set": {"hair_colour": "pink"}})

# documents variable which binds to all items from our collection
documents = coll.find({"nationality": "american"})

# iterate over each item in collection and print to console
for doc in documents:
    print(doc)
