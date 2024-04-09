#!/usr/bin/python

from os import environ


print("Content-Type: text/html\n\n")
print("<html><body>Hello %s!</body></html>" % environ.get('REMOTE_ADDR'))