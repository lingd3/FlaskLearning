#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import urllib


# post
params = urllib.urlencode({"praise":0, "user_id":1})
f = urllib.urlopen("http://127.0.0.1:5000/api/questions/2/comments", params)
print f.read()



