# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.admin import Admin
from flask.ext.admin.contrib.mongoengine import ModelView
from mongoengine import connect
from model.UserModel import User
from model.Lecture import Lecture, Section
from model.Post import Post
from view.Register import register
from view.Welcome import Welcome

app = Flask(__name__)
app.config.from_pyfile('auth.cfg')
connect(app.config.get("DB_NAME"), host='mongodb://' + app.config.get("DB_HOST_ADDRESS"))

app.register_blueprint(Welcome)
app.register_blueprint(register)

adminn = Admin(app)
adminn.add_view(ModelView(Lecture, "Lecture"))
adminn.add_view(ModelView(Post, "Post"))
adminn.add_view(ModelView(User, "User"))
adminn.add_view(ModelView(Section, "Sections"))

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)



