import pymongo
client = pymongo.MongoClient("mongodb+srv://Vignesh:Vignesh@cluster0.r0roayb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "Vignesh",
    "email": "vigneshthirunavukkarasu04@gmail.com",
    "surname" : "T"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
