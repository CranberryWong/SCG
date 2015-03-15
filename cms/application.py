#! /usr/bin/env python
#coding=utf-8

from urls import homeurls

import tornado.web
import os

SETTINGS = dict(
   debug = False,
   template_path = os.path.join(os.path.dirname(__file__),"templates"),
   static_path = os.path.join(os.path.dirname(__file__),"static"),
   cookie_secret = "dEr2Viz6TrqsoQVbQCRdxUmzKB5q40U0jYtp+fnsAOY=",
   login_url = "/signin",
   autoescape = None,
)

app = tornado.web.Application(
   handlers = homeurls,
   **SETTINGS
)
