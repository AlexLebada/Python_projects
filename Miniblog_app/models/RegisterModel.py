import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.miniblog
        self.Users = self.db.users

    def insert_user(self, data):
        #gensalt() method to encrypt with
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.Users.insert_one({"username": data.username,
                                "name": data.name,
                                "email": data.email,
                                "password": hashed
                                })
        print("uid is", id)
        if 1==0:
            myuser = self.Users.find_one({"username": data.username})

            if bcrypt.checkpw(str(data.password).encode(), myuser["password"]):
                print("this matches")