__author__ = 'alpan'
import urllib, urllib2
data = urllib.urlencode({'key': 'trnsl.1.1.20141114T220035Z.3425caccada41734.04a3758a1ff57b7f434f8cf711a04a4e34e2c43b', 'lang':'tr-en', 'text': 'alpankaraca tam bir ibne'})
u = urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate', data)
print u.read()