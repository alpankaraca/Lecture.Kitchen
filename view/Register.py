import hashlib

__author__ = 'cankemik'
from flask.views import View
from flask import  session , request , redirect , flash, url_for, render_template
from model.UserModel import User, login
from libs.UserLib import login_control
from libs.Render import render


class Register(View):
    methods = ["GET", "POST"]
    
    def dispatch_request(self):
        print "ilk"
        if request.method == "POST":
            print "ikinci"
            u = User()
            u.email = request.form.get('email')
            u.name = request.form.get('name')
            u.password = hashlib.md5(request.form.get('password')).hexdigest()
            u.save()
            durum = login(u.email, u.password)
            if durum:
                return render("welcome.html", user=u)
            else:
                return render("welcome.html", error=11)
        return render("single-product.html")

