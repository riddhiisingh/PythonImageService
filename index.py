import tornado.web
import tornado.ioloop

class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["imgfile"]
        for f in files:
            fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8883/img/{f.filename}")
    def get(self):
        self.render("index.html")

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8883)
    print("Listening on port")
    tornado.ioloop.IOLoop.instance().start()