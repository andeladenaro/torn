#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web

class GetResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self, path):
        body = self.controller.get()
        self.finish(body)

class PostResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def post(self, path):
        body = self.controller.post()
        self.finish(body)

class PutResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def put(self, path):
        body = self.controller.put()
        self.finish(body)

class PatchResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def patch(self, path):
        body = self.controller.patch()
        self.finish(body)

class DeleteResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def delete(self, path):
        body = self.controller.delete()
        self.finish(body)

