__author__ = 'alpan'


from flask import Flask
from mongoengine import connect
from libs.UserLib import is_user
from model.Lecture import Lecture, Section
from model.Post import Post

__author__ = 'alpan'
import urllib2
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)
app.config.from_pyfile('auth.cfg')
connect(app.config.get("DB_NAME"), host='mongodb://' + app.config.get("DB_HOST_ADDRESS"))

lectures = Lecture.objects(code__istartswith="l").all()

for l in lectures:
    if len(Lecture.objects(name__icontains=l.name).all()) > 1:
        print l.code, l.name
    #print l.code, l.name