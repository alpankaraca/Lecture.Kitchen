# -*- coding: utf-8 -*-
import hashlib
from libs.FlaskMail import Fmail

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

        u = User()
        u.username = request.form.get('username')
        u.email = request.form.get('email')
        u.password = hashlib.md5(request.form.get('password')).hexdigest()
        u.save()


        mail_data = {}
        mail_data["username"] = u.username
        mail_data["email"] = u.email + "@bilgiedu.net"
        mail_data["id"] = u.id

        Fmail({"title": "Lecture.Kitchen üyelik onay", "text": render_template("mail_verify_html.html", data=mail_data),
               "from_mail": u.email+"@bilgiedu.net"})


        print "at"

        return render("uyelik-onay.html", u=u)


        #durum = login(u.email, u.password)
        #if durum:
        #    return render("welcome.html" )
        #else:
        #    return render("welcome.html", error=11)
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


@register.route('/verify/<ids>', methods=['GET'])
def verify(ids):
    try:
        w = User.objects.get(id=ids)
    except:
        print "user verify edilmedi"
        return redirect("/?error=99")

    if w:
        w.verified_mail = True
        w.save()
        durum = login(w.email, w.password)
        print durum, "6666"
        if durum:
            print w.username, "----", request.path
            return redirect("/")
        print "verified user ", w.username
        return redirect("/register/verified")


@register.route('/verified', methods=['GET'])
def verified():

    return render("verified.html")


