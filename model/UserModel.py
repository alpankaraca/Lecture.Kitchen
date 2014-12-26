# -*- coding: utf-8 -*-
import hashlib
import datetime
from flask import request, session


__author__ = 'cankemik'

from mongoengine import document, fields

class User(document.Document):
    username = fields.StringField()
    name = fields.StringField()
    email = fields.StringField()
    password = fields.StringField()
    address = fields.StringField()
    city = fields.StringField()
    tel = fields.StringField()
    country = fields.StringField()
    fb_token = fields.StringField()
    last_visit = fields.StringField()
    fb_link = fields.StringField()

    def log(self, action, data={}):
        l = UserLog()
        l.user = self
        l.time = datetime.datetime.now()
        l.action = action
        l.data = data
        try:
            l.ip = request.remote_addr
        except:
            pass
        l.save()

    def login(self, email, password):
        if password == "facebook":
            data = User.objects.get(email=email)
            return data
        if len(password) == 32:
            password_hash = password
        else:
            password_hash = hashlib.md5(password).hexdigest()

        data = User.objects(email=email,password=password_hash)

        if data.all().count() > 0:
            data = data.get()
            return data

        return False


class UserLog(document.Document):
    user = fields.ReferenceField(User)
    time = fields.DateTimeField(default=datetime.datetime.now,required=True)
    action = fields.DictField()
    ip = fields.StringField()


def login(email, password):
    u=User()
    logindata = u.login(email, password)
    if logindata:
        session["lk_username"] = logindata.to_json()
        return True
    else:
        return False