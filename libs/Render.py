import json
from model.Lecture import Lecture
from model.UserModel import User

__author__ = 'cankemik'

from flask import render_template , redirect , request, session
from libs.UserLib import is_user


def render(*args, **kwargs):
    user = False
    if is_user():
        user_id = json.loads(session.get("lk_username")).get("_id")["$oid"]
        user = User.objects.get(id=user_id)

    recent = Lecture.objects.all().order_by("-last_updated")[:25]
    return render_template(recent=recent, user=user, *args, **kwargs)



