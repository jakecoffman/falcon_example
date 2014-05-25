import os
import json
import falcon
from wsgiref import simple_server


class Things:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps([{"id": 1, "name": "Thingie"}, {"id": 2, "name": "Thinger"}])


app = falcon.API()
app.add_route("/things", Things())


# This part is for convenience in development only
if __name__ == "__main__":
    def static(req, res):
        path = req.path.lstrip("/")
        if os.path.isfile(path):
            res.status = falcon.HTTP_200
            res.stream = open(path)
        else:
            res.status = falcon.HTTP_404


    class Index:
        def on_get(self, req, res):
            res.content_type = "text/html"
            res.status = falcon.HTTP_200
            res.stream = open(os.path.join("static", "index.html"))


    app.add_sink(static, "/static")
    app.add_route("/", Index())

    host = "127.0.0.1"
    port = 8000
    httpd = simple_server.make_server(host, port, app)
    print "Serving on %s:%s" % (host, port)
    httpd.serve_forever()
