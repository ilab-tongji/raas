from app import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

# this run file is used because there is some problem about flask when it comes to Original Access Control
# so I use the IOLoop of tornado to fix this problem

port = 5000

if __name__ == '__main__':

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=port)
    IOLoop.instance().start()