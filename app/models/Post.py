""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Post(Model):
    """Post Model"""
    __fillable__ = ["title", "body", "author_id"]

    @belongs_to("author_id", "id")
    def author(self):
        from app.models.User import User
        return User
