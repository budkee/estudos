#!/usr/bin/python


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<html><body>Hello %s</body></html>' % environ.get('REMOTE_ADDR')]