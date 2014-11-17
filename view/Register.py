import hashlib

__author__ = 'cankemik'
from flask.views import View
from flask import session, request, redirect, flash, url_for, render_template, Blueprint
from model.UserModel import User, login
from libs.UserLib import login_control
from libs.Render import render


register = Blueprint('register', __name__, template_folder="template_folder", url_prefix="/register")


@register.route('/regs', methods=["POST"])
def registerz():
    if request.method == "POST":
        print "at"
        u = User()
        u.username = request.form.get('username')
        u.email = request.form.get('email')
        u.name = request.form.get('name')
        u.password = hashlib.md5(request.form.get('password')).hexdigest()
        u.save()
        print "dasdasd"
        durum = login(u.email, u.password)
        if durum:
            return render("welcome.html", user=u)
        else:
            return render("welcome.html", error=11)
    return render("welcome.html")



@register.route('/login', methods=["POST"])
def loginz():
    if request.method == "POST":
        print "----", request
        path = request.form.get('path')
        username = request.form.get('username')
        password = hashlib.md5(request.form.get('password')).hexdigest()
        u = User.objects.get(username=username)
        print "dasdasd"
        durum = login(u.email, password)
        print durum, "6666"
        if durum:
            print u, "----", request.path
            return redirect(path)
        else:
            return render("welcome.html", error=11)
    return render("welcome.html")



@register.route('/logout', methods=["GET"])
def logoutz():
    session.pop('lk_username', None)
    return redirect("/")


