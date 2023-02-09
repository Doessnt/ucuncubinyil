import pymongo as pm

my_client = pm.MongoClient("mongodb://localhost:27017/")

mydb = my_client["ders"]

mycol = mydb["users"]
def user():
    dict = {"username":"Stalin", "password": "I'M_GAY"}
    execute = mycol.insert_one(dict)
    print(execute.inserted_id)

###DELETE###
"""
query = {"username": "does"}

mycol.delete_one(query)
doc = mycol.find()
for data in doc:
    print(data)


###UPDATE###

query = {"password":"231231"}
newquery = {"$set":{"password":"hitler_wasnt_right"}}

mycol.update_one(query,newquery)
for data in mycol.find():
    print(data)
"""


###LIMIT###

result = mycol.find().limit(2)