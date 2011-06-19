# Copyright (c) 2011, Ryan Bourgeois <bluedragonx@gmail.com>
# All rights reserved.
#
# This software is licensed under a modified BSD license as defined in the
# provided license file at the root of this project.  You may modify and/or
# distribute in accordance with those terms.
#
# This software is provided "as is" and any express or implied warranties,
# including, but not limited to, the implied warranties of merchantability and
# fitness for a particular purpose are disclaimed.

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget, authenticated_userid
from pyramid_couchauth_example.model import User

def login(context, request):
    if request.method != 'POST':
        return {'error': ''}
    if 'username' not in request.params:
        return {'error': 'Username is required.'}
    if 'password' not in request.params:
        return {'error': 'Password is required.'}
    
    username = request.params['username']
    password = request.params['password']

    users = User.view('pyramid/user_list', key=username)
    if len(users) == 0:
        return {'error': 'User not found.'}
    if not users.first().authenticate(password):
        return {'error': 'Bad password.'}

    headers = remember(request, username)
    redirect = '%s/auth/postlogin' % request.application_url
    return HTTPFound(location=redirect, headers=headers)

def logout(context, request):
    headers = forget(request)
    redirect = '%s/auth/postlogout' % request.application_url
    return HTTPFound(location=redirect, headers=headers)

def postlogin(context, request):
    username = authenticated_userid(request)
    if username is None:
        redirect = '%s/auth/login' % request.application_url
        return HTTPFound(location=redirect)
    return {}

def postlogout(context, request):
    return {}

