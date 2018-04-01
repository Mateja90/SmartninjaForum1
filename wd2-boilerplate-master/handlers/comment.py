from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment
from google.appengine.api import users
from google.appengine.api import memcache


class CommentHandler(BaseHandler):
    def post(self, topic_id):
        user=users.get_current_user()
        csrf_token=self.request.get("csrf_token")
        token=memcache.get(key=user.email())

        if not user:
            return self.write("You have to login to post something!")

        if token != csrf_token:
            return self.write("You are a hacker!")

        content= self.request.get("commenttext")
        topic=Topic.get_by_id(int(topic_id))

        new_comment= Comment(content=content, author_email=user.email(), topic_id=topic.key.id(), topic_title=topic.title)
        new_comment.put()
        return self.redirect_to("topic-details", topic_id=topic.key.id())
