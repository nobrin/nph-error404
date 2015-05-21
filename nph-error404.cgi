#!/usr/bin/env python
import os, time, urllib
from datetime import datetime

def unquote_uri(uri):
    rawuri = urllib.unquote(uri)
    return rawuri.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

requri = os.environ.get("REQUEST_URI", "/").split("?", 1)[0]
param = {
    "SERVER_PROTOCOL": os.environ.get("SERVER_PROTOCOL", "HTTP/0.9"),
    "REQUEST_URI"    : unquote_uri(requri),
    "TIMESTAMP"      : datetime(*time.gmtime()[:6]).strftime("%a, %d %b %Y %H:%M:%S GMT"),
}

head = """%(SERVER_PROTOCOL)s 404 Not Found
Date: %(TIMESTAMP)s
Server: Apache
Content-Length: %(CONTENT_LENGTH)d
Connection: close
Content-Type: text/html; charset=iso-8859-1"""

body = """<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL %(REQUEST_URI)s was not found on this server.</p>
</body></html>""" % param

param["CONTENT_LENGTH"] = len(body)

print head % param
print ""
print body

