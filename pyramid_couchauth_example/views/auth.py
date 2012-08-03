# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.
"""
Define auth actions.
"""

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget, authenticated_userid
from pyramid_couchauth_example.model import User


def login(context, request):
    """Display a login prompt."""
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
    """Handle logout action."""
    headers = forget(request)
    redirect = '%s/auth/postlogout' % request.application_url
    return HTTPFound(location=redirect, headers=headers)


def postlogin(context, request):
    """Handle login action and display post-login "welcome" page."""
    username = authenticated_userid(request)
    if username is None:
        redirect = '%s/auth/login' % request.application_url
        return HTTPFound(location=redirect)
    return {}


def postlogout(context, request):
    """Display post-logout "goodbye" page."""
    return {}

