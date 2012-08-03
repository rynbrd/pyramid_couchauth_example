# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.

from pyramid.response import Response
from pyramid.security import authenticated_userid

def root(context, request):
    return {'project': 'pyramid_couchauth_example'}

def forbidden(context, request):
    username = authenticated_userid(request)
    if username is None:
        username = ""
    return {'username': username}

