from flask import Flask
from mongoengine import connect
from model.Lecture import Lecture

__author__ = 'alpan'
import urllib2
from BeautifulSoup import BeautifulSoup

app = Flask(__name__)
app.config.from_pyfile('../auth.cfg')
connect(app.config.get("DB_NAME"), host='mongodb://' + app.config.get("DB_HOST_ADDRESS"))


proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
html = urllib2.urlopen("https://sis.bilgi.edu.tr/Curriculum/REGLINK_LisansCourseSchedule.htm").read()
#html = urllib.urlopen('http://stackoverflow.com/questions/9758500/python-read-html-source-from-url-and-get-date-into-program')
#soup = BeautifulSoup(html)

lectures = []

text = html
for i in text.split('class="TR0">'):
    row = i.split('</TR>')[0]
    #for cell in row.split('&nbsp;&nbsp;'):
    #    print cell.split("</TD>")[0].split("\n")[0], " ----",

    tmp_text = ""
    try:
        tmp_text = row.split('&nbsp;&nbsp;')[1].split("</TD>")[0].split(".")[0]#.split("\n")[0]

        tmp_text += " - " + row.split('&nbsp;&nbsp;')[2].split("</TD>")[0]#.split("\n")[0]
        tmp_text += " - " + row.split('&nbsp;&nbsp;')[3].split("</TD>")[0]#.split("\n")[0]
    except:
        print "except"
    if tmp_text:
        if tmp_text not in lectures:
            #print tmp_text
            lectures.append(tmp_text)
    #print row[2].split('&nbsp;&nbsp;')[0].split("</TD>")[0].split("\n")[0]
    #print row[3].split('&nbsp;&nbsp;')[0].split("</TD>")[0].split("\n")[0]
    #print row[1].split('&nbsp;&nbsp;').split("</TD>")[0].split("\n")[0]
    #print row[2].split('&nbsp;&nbsp;').split("</TD>")[0].split("\n")[0]
    #print row[3].split('&nbsp;&nbsp;').split("</TD>")[0].split("\n")[0]


#print lectures
count = 0
for ll in lectures:
    #print lectures[count], "-----------------", ll
    try:
        if lectures[count].split(" - ")[0] == lectures[count+1].split(" - ")[0]:
            #print lectures[count].split(" - ")[0], "---", lectures[count+1].split(" - ")[0]
#            print count,lectures[count],
            print lectures[count].split(" - ")[0]
            del lectures[count]
            print lectures[count].split(" - ")[0],
    except:
        print "except"
    count += 1

print lectures

Lecture.objects.all().delete()
for lec in lectures:
    print lec
    l = Lecture()
    try:
        l = Lecture.objects.get(name=lec.split(" - ")[0])
    except:
        pass
    l.name = lec.split(" - ")[0]
    l.lecturer = lec.split(" - ")[1]
    l.program = lec.split(" - ")[2]
    l.slug = lec.split(" - ")[0].split(" ")[0] + "_" + lec.split(" - ")[0].split(" ")[1]
    l.save()
    print l
    print "---"

print Lecture.objects.all()