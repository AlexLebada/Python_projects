import pymongo, bcrypt
from pymongo import MongoClient

class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.miniblog
        self.Users = self.db.users

    def check_user(self, data, log_typ):
        user = self.Users.find_one({"username": data.username})
        if user and log_typ == 0:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                #print("good")
                return user
            else:
                # print("wrong")
                return False
        elif user and log_typ == 1:
                return user

        else:
            #print("wrong")
            return False


    def update_info(self, data):
        updated = self.Users.update_one({
            "username": data["username"]
        },{"$set": data}) # $set method updates the DB fields or creates them from data key-value pair

        return True


    def get_profile(self, user):
        user_info = self.Users.find_one({"username": user})
        print(type(user_info))
        return user_info


    def update_image(self, update):
        updated = self.Users.update_one({"username": update["username"]},
                                       {"$set": {update["type"]: update[update["type"]]}})

        return updated
