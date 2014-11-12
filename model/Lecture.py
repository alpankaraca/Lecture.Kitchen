from model.Post import Post

__author__ = 'alpan'
from mongoengine import document, fields


class Lecture(document.Document):
    name = fields.StringField()
    slug = fields.StringField()
    lecturer = fields.StringField()
    program = fields.StringField()
    posts = fields.ListField(fields.ReferenceField(Post))


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name