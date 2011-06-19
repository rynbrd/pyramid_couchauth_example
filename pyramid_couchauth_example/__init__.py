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

from pyramid.config import Configurator
from pyramid.exceptions import Forbidden
from pyramid_couchauth_example.resources import get_root
from pyramid_couchauth_example.model import init_model, Session
from pyramid_couchauth.identification import AuthTktIdentifier
from pyramid_couchauth.authentication import CouchAuthenticationPolicy
from pyramid_couchauth.authorization import CouchAuthorizationPolicy

def main(global_config, **settings):
    init_model(settings)

    """
    Set up couchauth. Use authtkt for the identifier.
    """
    identifier = AuthTktIdentifier('sekret')
    authentication = CouchAuthenticationPolicy(Session.auth, identifier)
    authorization = CouchAuthorizationPolicy(Session.auth)

    """
    Configure the application with couchdb auth.
    """
    config = Configurator(root_factory=get_root, settings=settings,
        authentication_policy=authentication,
        authorization_policy=authorization)

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

