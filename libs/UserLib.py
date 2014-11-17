__author__ = 'cankemik'
from flask import  session
from model.UserModel import User
import json

def login_control(email,password):
    user = User.objects.filter(email=email, password=password).all()
    if user.count()>0:
        session["lk_username"] = user[0]
        return True
    return False

def is_user():
    if session.get("lk_username"):
        #print json.loads(session.get("suphi_username")).get("_id")["$oid"]
        user = User.objects.get(id=json.loads(session.get("lk_username")).get("_id")["$oid"])
        return user
    return False