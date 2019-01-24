#!/usr/bin/env python
# -*- coding: utf-8 -*-

from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from datetime import datetime


def hello_world(request):
    print('Incoming request', str(request.GET) )
    return Response("<h1>Hello World!</h1><p>This is my first Python Website.</p><h2><strong>:)</strong></h2>")

def notfound(request):
    return Response(f"<h1>Not Found</h1><p>The requested URL '{request.environ['PATH_INFO']}' was not found.</p><h2><strong>:(</strong></h2>")


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        config.add_view(notfound, context='pyramid.httpexceptions.HTTPNotFound')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
