# pip install cloudant or on my RPi sudo pip3 install cloudant  

# from cloudant.client import Cloudant
from cloudant.client import CouchDB 

def couchdb_connect(USER, PASSWORD, DB_URL):
    """Connects to the couch database."""
    global couchDB_client
    # check if a connection to the database is already established 
    try: 
        couchDB_client
    except NameError:
        print("Conecting to the DB...")
        # In order to manage a connection you must first initialise the connection by constructing either a Cloudant or CouchDB client. 
        # couchDB_client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME, connect=True)
        couchDB_client = CouchDB(USER, PASSWORD, url=DB_URL, connect=True)
    else:
        print("DB conection already established.")


def couchdb_post(db_name, data, verify):
    """Add a document to a specified database

    Parameters:
    argument1 (string): Your database name
    argument2 (dict): Your database data in a dictionary. Setting _id is optional
    argument3 (bool): Whether you want verification. 
    """
    # Open an existing database, for example, I have customers
    my_database = couchDB_client[db_name]
    # Create a document using the Database API
    my_document = my_database.create_document(data)

    # perform output check
    if verify:
        if my_document.exists():
            print('Document was submitted to the DB.')
 

# Lets test it
# x = {"sensorHumanId": "Leon", "sensorUuid": "123456778890", "temperatureValue": "-22", "recordedDate": "2019-09-30 13:21"}
#couchdb_connect('admin', 'password', 'http://192.168.1.109:5984')
#couchdb_post('temperature', {"sensorHumanId": "Leon", "sensorUuid": "123456778890", "temperatureValue": "1", "recordedDate": "2019-09-30 13:21"}, True)
# should say: DB conection already established
