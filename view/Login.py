# -*- coding: utf-8 -*-
__author__ = 'cankemik'
from flask.views import View
from Libs.UserLib import *
from flask import Flask,flash, redirect, render_template, \
     request, url_for, Blueprint
from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
FACEBOOK_APP_ID = '254292284695105'
FACEBOOK_APP_SECRET = 'eeb79fc3bffffdd999563ed3c58b2a4f'
oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

