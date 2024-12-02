import web
from models import RegisterModel, LoginModel, Posts
from pathlib import Path
import os

web.config.debug = False # because interfere with sessions

urls = (
    '/', 'home',
    '/register', 'register',
    '/logout', 'Logout',
    '/settings', 'UserSettings',
    '/update-settings', 'UpdateSettings',
    '/postregistration', 'PostRegistration',
    '/profile/(.*)/info', "UserInfo",   # this is to display selected user's profile
    '/check-login', 'CheckLogin',
    '/login', 'Login',
    '/post-activity', 'Posting',
    '/upload-image/(.*)', "UploadImage",
    '/profile/(.*)', "UserProfile" # is below the similar router with /info because it will direct to the nearest similar route
)


app = web.application(urls, globals())
# diskstore() - where cookies are stored ?
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer # ?
# by using globals param. session methodis maintained through every route, without passing anything
render = web.template.render("views/templates/",
                             base="MainLayout",
                             globals={'session': session_data,
                                      'current_user': session_data["user"]})


class home:
    def GET(self):
        post = Posts.PostsModel()
        posts = post.get_all_posts()
        return render.Home(posts)


class register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        #print(type(data))
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data, 0)
        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect
        return "error"


class Posting:
    def POST(self):
        data = web.input() # here data is what user is posting in the form not user login
        data.username = session_data['user']['username']
        post = Posts.PostsModel()
        post.insert_post(data)
        return "success" # into browser console


class UserProfile: # user activity
    def GET(self, user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile((user))
        post = Posts.PostsModel()
        posts = post.get_user_posts(user)
        return render.Profile(posts, user_info)


class UserInfo:
    def GET(self, user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)
        return render.Info(user_info)

class UserSettings:
    def GET(self):
        return render.Settings()


class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]
        settings = LoginModel.LoginModel()
        if settings.update_info(data):
            updated_user = settings.check_user(data, 1)
            if updated_user:
                session_data["user"] = updated_user
            return "success"
        else:
            return "A fatal error has occurred"

class Logout:
    def GET(self):
        session['user'] = None # somehow value is None but in Home page for example is option different from None
        session_data['user'] = None
        session.kill()
        return "success"


import os
import web
from pathlib import Path  # Use pathlib for better path management


class UploadImage:
    def POST(self, type):
        file = web.input(avatar={}, background={})
        file_dir = os.getcwd() + "/static/uploads/" + session_data["user"]["username"] # cwd - current working dir
        print(file_dir)
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        if "avatar" or "background" in file:
            filepath = file[type].filename.replace('\\', '/')
            filename = filepath.split("/")[-1]
            #update the current file
            f = open(file_dir + "/" + filename, 'wb') # wb - binary mode
            f.write(file[type].file.read())
            f.close()

            update = {}
            update["type"] = type
            update[type] = '/static/uploads/' + session_data["user"]["username"] + "/" + filename
            update["username"] = session_data["user"]["username"]
            account_model = LoginModel.LoginModel()
            update_avatar = account_model.update_image(update)

        raise web.seeother("/settings") # jump to settings page after upload



if __name__ == "__main__":
    app.run()