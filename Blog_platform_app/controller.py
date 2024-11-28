import web
from models import RegisterModel, LoginModel

web.config.debug = False # because interfere with sessions

urls = (
    '/', 'home',
    '/register', 'register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin'
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
        data = type('obj', (object,), {"username": "alexxzor", "password": "asd"})
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        return render.Home()


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
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect
        return "error"

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

if __name__ == "__main__":
    app.run()