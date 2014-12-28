import datetime
from model.UserModel import User

__author__ = 'alpan'
from mongoengine import document, fields


class Post(document.Document):
    user = fields.ReferenceField(User)
    username = fields.StringField()
    _created_date = fields.DateTimeField(default=datetime.datetime.now())
    content = fields.StringField()
    rank = fields.IntField()
    _is_deleted = fields.BooleanField()
    lang = fields.StringField()

    #def save(self, *args, **kwargs):
    #    #import urllib, urllib2, json
    #    #data = urllib.urlencode({'key': 'be7406c272d8a64b30429b56e0f9ec63', 'q': self.content})
    #    #u = urllib2.urlopen('http://ws.detectlanguage.com/0.2/detect', data).read()
    #    #print u
    #    #print json.loads(u)[u"data"][u"detections"][0][u"language"]
    #    #self.lang = json.loads(u)[u"data"][u"detections"][0][u"language"]
#
    #    return super(Post, self).save(*args, **kwargs)