# coding: utf-8

import logging

import tornado.ioloop
import tornado.web
import tornado.wsgi

logger = logging.getLogger()


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        headers = {h[0]: h[1] for h in self.request.headers.get_all()}
        
        logger.debug(self.request.method)
        logger.debug(self.request.uri)
        logger.debug("Headers---------")
        logger.debug(headers)
        logger.debug("Body-----------")
        logger.debug(self.request.body)
        self.write({
            "path": self.request.uri,
            "method": self.request.method,
            "headers": headers,
            "body": self.request.body,
        })

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


application = tornado.web.Application([
    (r"/.*", MainHandler),
])

app = tornado.wsgi.WSGIAdapter(application)
