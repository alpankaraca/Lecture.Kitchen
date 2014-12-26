# -*- coding: utf-8 -*-
import urllib
from flask import Flask
from mongoengine import connect
from libs.UserLib import is_user
from model.Lecture import Lecture
from model.Post import Post

__author__ = 'alpan'
import urllib2
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)
app.config.from_pyfile('auth.cfg')
connect(app.config.get("DB_NAME"), host='mongodb://' + app.config.get("DB_HOST_ADDRESS"))


proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
html = urllib2.urlopen("https://sis.bilgi.edu.tr/Curriculum/REGLINK_LisansCourseSchedule.htm").read()
#html = urllib.urlopen('http://stackoverflow.com/questions/9758500/python-read-html-source-from-url-and-get-date-into-program')
#soup = BeautifulSoup(html)


#posts = Post.objects.all()
#for p in posts:
#    p.user = is_user()
#    p.save()




lectures = []

text = html
for h in text.split('<tr class="TR'):
    for i in h.split('0">'):
        row = i.split('</TR>')[0]
        print row
        tmp_text = ""
        try:
            tmp_text = row.split('&nbsp;&nbsp;')[1].split("</TD>")[0].split(".")[0]#.split("\n")[0]
            tmp_text += " - " + row.split('&nbsp;&nbsp;')[2].split("</TD>")[0]#.split("\n")[0]
            tmp_text += " - " + row.split('&nbsp;&nbsp;')[3].split("</TD>")[0]#.split("\n")[0]
        except:
            print "except"
        if tmp_text:
            print tmp_text
            if tmp_text not in lectures:
                lectures.append(tmp_text)
    for i in h.split('style="color:white;font-size:14px;">&nbsp;'):
        row = i.split('</a></TD>')[0]
        print row


#count = 0
#for ll in lectures:
#    try:
#        if lectures[count].split(" - ")[0] == lectures[count+1].split(" - ")[0]:
#            print lectures[count].split(" - ")[0]
#            del lectures[count]
#            print lectures[count].split(" - ")[0],
#    except:
#        print "except"
#    count += 1
#
#print lectures
#
#Lecture.objects.all().delete()
#for lec in lectures:
#    print lec
#    l = Lecture()
#    try:
#        l = Lecture.objects.get(name=lec.split(" - ")[0])
#    except:
#        pass
#    l.name = lec.split(" - ")[0]
#    l.lecturer = lec.split(" - ")[1]
#    l.program = lec.split(" - ")[2]
#    l.slug = lec.split(" - ")[0].split(" ")[0] + "_" + lec.split(" - ")[0].split(" ")[1]
#    l.save()
#    print l
#    print "---"
#
#print Lecture.objects.all()