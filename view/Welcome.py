from flask import render_template, Blueprint, request, redirect
from flask.views import View
from model.Lecture import Lecture
from model.Post import Post

__author__ = 'alpan'

Welcome = Blueprint('Welcome', __name__, template_folder="template_folder", url_prefix="")

@Welcome.route('/', methods=["GET", "POST"])
def welcome():
    lec = Lecture.objects.all()
    for l in Lecture.objects.all():
        print l.slug
    return render_template("welcome.html", isUser=True, lec=lec)

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
    return render_template("post.html", lec=lec, posts=posts, isUser=True)

@Welcome.route('/lecture/<slg>', methods=["GET", "POST"])
def lecture(slg):
    lec = Lecture.objects.get(slug=slg)

    if request.args.get("addPost"):
        text = request.form.get("post")
        lec = Lecture.objects.get(id=request.form.get("lec_id"))
        print lec
        p = Post()
        p.content = text
        p.save()
        lec.posts.append(p)
        lec.save()
        posts = lec.posts
        return render_template("post.html", lec=lec, posts=posts, isUser=True)

    if len(lec.posts) > 0:
        posts = lec.posts
    else:
        posts = 0
    print posts
    return render_template("post.html", lec=lec, posts=posts, isUser=True)

@Welcome.route('/search', methods=["GET", "POST"])
def search():
    import json
    if request.args.get("text"):
        name = request.args.get("text")
        lectures = Lecture.objects(name__istartswith=name).all()
        print lectures
        return lectures.to_json()

    text = request.form.get("lecture")
    #lec = Lecture.objects.get(name=text)
    #if len(lec.posts) == 0:
    #    return render_template("/"+lec.slug, posts=0, isUser=True)
    #else:
    #    return render_template("/"+lec.slug, posts=lec.posts, isUser=True)
    return "ok"
