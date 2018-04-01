import os
import jinja2
import webapp2

from handlers.base import BaseHandler, MainHandler, CookieAlertHandler
from handlers.topic import TopicHandler, TopicDetailHandler
from handlers.comment import CommentHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler),
    webapp2.Route('/topic/add', TopicHandler, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetailHandler, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentHandler, name="comment-add"),

], debug=True)
