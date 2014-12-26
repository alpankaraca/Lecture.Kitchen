from datetime import datetime
from model.Post import Post

__author__ = 'alpan'
from mongoengine import document, fields, EmbeddedDocumentField


class Lecture(document.Document):
    name = fields.StringField()
    slug = fields.StringField()
    lecturer = fields.StringField()
    program = fields.StringField()
    posts = fields.ListField(EmbeddedDocumentField(Post))
    last_updated = fields.DateTimeField()

    def save(self, *args, **kwargs):
        self.last_updated = datetime.now()

        return super(Lecture, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name