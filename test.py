import pymongo
client = pymongo.MongoClient("mongodb+srv://likhithahemanth:Amlpl3425B@cluster0.g4p3bvk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"likhitha" ,
    "email":"likhitha.m37@gmail.com" ,
    "surname":"gowda"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)