from datetime import datetime
from django.template.defaultfilters import slugify
from model.Post import Post

__author__ = 'alpan'
from mongoengine import document, fields, EmbeddedDocumentField, EmbeddedDocument


class Section(document.Document):
    code = fields.StringField()
    lecturer = fields.StringField()
    schedule = fields.StringField()


class Lecture(document.Document):
    code = fields.StringField()
    name = fields.StringField()
    slug = fields.StringField()
    sections = fields.ListField(fields.ReferenceField(Section))
    posts = fields.ListField(fields.ReferenceField(Post))
    last_updated = fields.DateTimeField()

    def save(self, *args, **kwargs):
        self.last_updated = datetime.now()
        self.slug = slugify(self.code)

        return super(Lecture, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name