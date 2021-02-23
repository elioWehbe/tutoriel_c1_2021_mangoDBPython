def getDataBase():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db


def addClient(db):
    db.clients.insert_one({"name": "X"})


def getClient(db):
    return db.clients.find_one()

def deleteClient(db):
    db.clients.delete_one({"name": "X"})

if __name__ == "__main__":
    dataBase = getDataBase()
    addClient(dataBase)
    print(getClient(dataBase))
