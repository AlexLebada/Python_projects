import datetime
import humanize
import pymongo, bcrypt
from pymongo import MongoClient

class PostsModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.miniblog
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert_one({"username": data.username, "content": data.content, "date_added": datetime.datetime.now()})
        post = self.Posts.find_one({"_id": inserted.inserted_id})
        return post

    def get_all_posts(self):
        all_posts = self.Posts.find().sort("date_added", -1)
        custom_posts = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            if "date_added" in post and post["date_added"] is not None:
                post["timestamp"] = humanize.naturaltime(datetime.datetime.now() - post["date_added"])
            else:
                post["timestamp"] = humanize.naturaltime(datetime.datetime.now())
            custom_posts.append(post)

        return custom_posts

    def get_user_posts(self, user):
        all_posts = self.Posts.find({"username": user}).sort("date_added", -1)
        new_posts = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)

        return new_posts