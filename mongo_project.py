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


# helper function to find records for read, update or delete operations
def get_record():
    print("")
    # prompt user for first and last names
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        # searching the database for names given
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")
    # if no results found print another error message
    if not doc:
        print("")
        print("Error! No results found")

    return doc


# function to take inputs from user and add to new db record
def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        # doc.items() method returns key value pairs of a dictionary
        # as tuples in a list
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


# function which calls show_menu() and processes user selection
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid option")
        print("")


# function to find and update records per user inputs
def edit_record():
    doc = get_record()
    if doc:
        # declare empty dictionary update_doc - add names to this dictionary
        # while iterating over key/value pairs
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                # for fields != "_id" take user input for fields to be updated
                update_doc[k] = input(k.capitalize() + " [" + v + "] >")

        # if no user input given to update a value assign existing value to key
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input(
            "Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted")
            except:
                print("Error accessing the datebase")
        else:
            print("Document not deleted")

# call mongo connection and create celebrities collection
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
