from flask import render_template, Blueprint, request, redirect, jsonify
from flask.views import View
from libs.Render import render
from libs.UserLib import is_user
from model.Lecture import Lecture
from model.Post import Post
from model.UserModel import User

__author__ = 'alpan'

Welcome = Blueprint('Welcome', __name__, template_folder="template_folder", url_prefix="")

@Welcome.route('/', methods=["GET", "POST"])
def welcome():

    posts = Post.objects.all()
    for p in posts:
        p.user = is_user()
        p.save()
    return render("welcome.html", isUser=True)

@Welcome.route('/addPost', methods=["GET", "POST"])
def add_post():
    print("addpost")
    text = request.form.get("post")
    lec = Lecture.objects.get(id=request.form.get("lec_id"))
    print lec
    p = Post()
    p.content = text
    p.save()
    lec.posts.append(p)
    lec.save()
    posts = lec.posts
    return render("post.html", lec=lec, posts=posts, isUser=True)

@Welcome.route('/lecture/<slg>', methods=["GET", "POST"])
def lecture(slg):
    lec = Lecture.objects.get(slug=slg)

    if request.args.get("addPost"):
        text = request.form.get("post")
        lec = Lecture.objects.get(id=request.form.get("lec_id"))
        u = User.objects.get(id=request.form.get("user_id"))
        p = Post()
        p.content = text
        print u == is_user()
        p.user = u
        p.save()
        lec.posts.append(p)
        lec.save()
        posts = lec.posts
        return render("post.html", lec=lec, posts=posts, isUser=True)

    if len(lec.posts) > 0:
        posts = lec.posts
    else:
        posts = 0
    print posts
    return render("post.html", lec=lec, posts=posts, isUser=True)

@Welcome.route('/search', methods=["GET", "POST"])
def search():
    import json
    if request.args.get("text"):
        name = request.args.get("text")
        lectures = Lecture.objects(name__istartswith=name).all()
        return lectures.to_json()

    text = request.form.get("lecture")
    #lec = Lecture.objects.get(name=text)
    #if len(lec.posts) == 0:
    #    return render("/"+lec.slug, posts=0, isUser=True)
    #else:
    #    return render("/"+lec.slug, posts=lec.posts, isUser=True)
    return "ok"


@Welcome.route('/translate', methods=["GET", "POST"])
def translate():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    import json
    if request.args.get("lang"):
        lang = request.args.get("lang")
        text = Post.objects.get(id=request.args.get("id")).content
        import urllib, urllib2
        data = urllib.urlencode({'key': 'trnsl.1.1.20141114T220035Z.3425caccada41734.04a3758a1ff57b7f434f8cf711a04a4e34e2c43b', 'lang':'tr-'+str(lang), 'text': text})
        print data
        u = urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate', data)
        return u.read()
    return "ok"
