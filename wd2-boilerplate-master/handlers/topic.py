from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment
from google.appengine.api import users
from google.appengine.api import memcache
import uuid
class TopicHandler(BaseHandler):
    def get(self):
        csrf_token =str(uuid.uuid4())
        user=users.get_current_user()
        memcache.delete(key=user.email())
        memcache.add(key=csrf_token, value=user.email(), time=600)

        params = {"token": csrf_token}
        return self.render_template("topic_add.html", params=params)

    def post(self):
        user = users.get_current_user()
        csrf_token = self.request.get("csrf_token")
        token = memcache.get(key=csrf_token)
        if not user:
            return self.write("You have to login before you can post a topic!")

        if token != user.email():
            return self.write("You are hacker!")
        title = self.request.get("title")
        content = self.request.get("text")

        new_topic = Topic(title=title, content=content, author_email=user.email())
        new_topic.put()

        return self.redirect_to("topic-details", topic_id=new_topic.key.id())

class TopicDetailHandler(BaseHandler):
    def get(self, topic_id):
        user=users.get_current_user()
        topic = Topic.get_by_id(int(topic_id))
        comments=Comment.query(Comment.topic_id==topic.key.id(), Comment.deleted==False).order(Comment.created).fetch()
        csrf_token=str(uuid.uuid4())
        memcache.delete(key=user.email())
        memcache.add(key=user.email(), value=csrf_token, time=600)
        params={"topic": topic, "comments": comments, "csrf_token": csrf_token}
        return self.render_template("topic_details.html", params=params)
