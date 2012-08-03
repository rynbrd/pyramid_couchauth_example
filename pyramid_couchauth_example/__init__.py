# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.
"""
Application entry point.
"""

from pyramid.config import Configurator
from pyramid.exceptions import Forbidden
from pyramid_couchauth_example.resources import get_root
from pyramid_couchauth_example.model import init_model, Session
import pyramid_couchauth

def main(global_config, **settings):
    """Application entry point."""
    init_model(settings)

    """
    Configure the application with couchdb auth.
    """
    config = Configurator(root_factory=get_root, settings=settings)

    """
    Set up couchauth.
    """
    pyramid_couchauth.configure(config, Session.auth)

    """
    Set up all of our views.
    """
    config.add_view('pyramid_couchauth_example.views.forbidden',
        context=Forbidden,
        renderer='pyramid_couchauth_example:templates/forbidden.mako')
    config.add_view('pyramid_couchauth_example.views.root',
        context='pyramid_couchauth_example:resources.Root',
        renderer='pyramid_couchauth_example:templates/root.pt')
    config.add_view('pyramid_couchauth_example.views.auth.login',
        name='login',
        context='pyramid_couchauth_example:resources.Auth',
        renderer='pyramid_couchauth_example:templates/auth/login.mako')
    config.add_view('pyramid_couchauth_example.views.auth.logout',
        name='logout',
        context='pyramid_couchauth_example:resources.Auth')
    config.add_view('pyramid_couchauth_example.views.auth.postlogin',
        name='postlogin',
        context='pyramid_couchauth_example:resources.Auth',
        renderer='pyramid_couchauth_example:templates/auth/postlogin.mako')
    config.add_view('pyramid_couchauth_example.views.auth.postlogout',
        name='postlogout',
        context='pyramid_couchauth_example:resources.Auth',
        renderer='pyramid_couchauth_example:templates/auth/postlogout.mako')
    config.add_view('pyramid_couchauth_example.views.page.public',
        name='',
        context='pyramid_couchauth_example:resources.Page',
        renderer='pyramid_couchauth_example:templates/page/public.mako')
    config.add_view('pyramid_couchauth_example.views.page.public',
        name='public',
        context='pyramid_couchauth_example:resources.Page',
        renderer='pyramid_couchauth_example:templates/page/public.mako')
    config.add_view('pyramid_couchauth_example.views.page.private',
        name='private',
        context='pyramid_couchauth_example:resources.Page',
        renderer='pyramid_couchauth_example:templates/page/private.mako',
        permission='superpowers')
    config.add_static_view('static', 'pyramid_couchauth_example:static')
    return config.make_wsgi_app()

