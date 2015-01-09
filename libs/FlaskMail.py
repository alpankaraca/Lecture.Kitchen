from flask import current_app
from flask.ext.mail import Mail, Message

__author__ = 'cankemik'


def Fmail(data):
    user = current_app.config.get("MAIL_USER")
    passwd = current_app.config.get("MAIL_PASSWORD")

    from_addr = current_app.config.get("MAIL_USER")
    to_addr = data.get("from_mail")
    mail = Mail(current_app)
    current_app.config.update(
        MAIL_SERVER='smtp.yandex.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='no-reply@lecture.kitchen',
        MAIL_PASSWORD='8Jy90_V!2'
    )
    bcc = "alpann@gmail.com"
    mail.init_app(current_app)
    try:
        msg = Message('Lecture.Kitchen', sender='no-reply@lecture.kitchen', recipients=[to_addr],
                      bcc=[bcc])
        msg.html = data.get("text")
        mail.send(msg)
    except:
        print "olmadi"
    return "ok"


def UserMail(user, passwd, smtp, smtp_port, smtp_tsl, smtp_auth, data):
    mail_user = user
    mail_passwd = passwd
    print "--- DEBUG ---"
    print "--- DEBUG ---"
    print data
    print "--- DEBUG ---"
    print "--- DEBUG ---"
    from_addr = user
    to_addr = ';'.join(data.get("from_mail"))
    print to_addr
    mail = Mail(current_app)
    current_app.config.update(
        MAIL_SERVER=smtp,
        MAIL_PORT=smtp_port,
        MAIL_USE_SSL=smtp_auth,
        MAIL_USE_TLS=smtp_tsl,
        MAIL_USERNAME=mail_user,
        MAIL_PASSWORD=mail_passwd
    )
    mail.init_app(current_app)
    msg = Message('Reztoran', sender=from_addr, recipients=to_addr.split(";"))
    msg.html = data.get("text")
    msg.subject = data.get('title')
    mail.send(msg)
    return "ok"

