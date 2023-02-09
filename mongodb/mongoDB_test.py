import pymongo as pm

my_client = pm.MongoClient("mongodb://localhost:27017/")
mydb = my_client["ders"]

mycol = mydb["users"]

def user():
    i = 0
    for i in range(2):
        if i == 0:
            dict = {"username":"bsrzz", "password": "hitler_wasnt_right"}
            execute = mycol.insert_one(dict)
            print(execute.inserted_id)
        elif i == 1:
            dict = {"username": "hitler", "password": "hitler_was_right"}
            execute = mycol.insert_one(dict)
            print(execute.inserted_id)
    i += 1
user()

query = {"password":"hitler_wasnt_right"}
newquery = {"$set":{"password":"hitler_was_right"}}

mycol.update_one(query,newquery)
