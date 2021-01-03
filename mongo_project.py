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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e


# function to display menu
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


# function which displays our menu and processes user selection
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have select option 1")
        elif option == "2":
            print("You have select option 2")
        elif option == "3":
            print("You have select option 3")
        elif option == "4":
            print("You have select option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid option")
        print("")


# call mongo connection and create celebrities collection
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
