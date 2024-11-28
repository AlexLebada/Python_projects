import web

# if first element which is url is accesed, look for index class
urls = (
    '/(.*)/(.*)', 'index'
)
# render html content
render = web.template.render("resources/")
# instantiate web app
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return  render.main(name, age)

if __name__ == "__main__":
    app.run()