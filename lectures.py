# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.mongoengine import ModelView
from mongoengine import connect
from model.Lecture import Lecture
from view.Welcome import Welcome

app = Flask(__name__)
app.config.from_pyfile('auth.cfg')
connect(app.config.get("DB_NAME"), host='mongodb://' + app.config.get("DB_HOST_ADDRESS"))

app.register_blueprint(Welcome)

adminn = Admin(app)
adminn.add_view(ModelView(Lecture, "Lecture"))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
