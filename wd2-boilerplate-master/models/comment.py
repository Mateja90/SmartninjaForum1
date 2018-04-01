from google.appengine.ext import ndb

class Comment(ndb.Model):
    author_email = ndb.StringProperty()
    content = ndb.TextProperty()
    topic_id = ndb.IntegerProperty()
    topic_title = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default = False)
