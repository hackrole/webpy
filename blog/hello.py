#!/usr/bin/python2.7
#charset=utf-8

import web

render = web.template.render('template/')

urls = (
    "/hello", "hello"
    )
urls += (
    "/hello2", "helloTemplate"
    )

class helloTemplate:
    def GET(self):
        name = "hackrole"
        return render.hello(name)

class hello:
    def GET(self):
        return 'hello, world!'
    

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
