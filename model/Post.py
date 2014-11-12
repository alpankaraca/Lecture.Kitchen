from datetime import datetime
from model.UserModel import User

__author__ = 'alpan'
from mongoengine import document, fields


class Post(document.Document):
    user = fields.ReferenceField(User)
    _created_date = fields.DateTimeField(default=datetime.now())
    content = fields.StringField()
    rank = fields.IntField()
    _is_deleted = fields.BooleanField()