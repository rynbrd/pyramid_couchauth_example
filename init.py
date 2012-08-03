# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.

import os, sys, pkg_resources
from paste.deploy.loadwsgi import appconfig
from pyramid_couchauth_example.model import Session, init_model
from pyramid_couchauth_example.model import User, Group, Permission
from couchdbkit.loaders import FileSystemDocsLoader

def setup_app(settings):
    # Init CouchDB model.
    print('initializing model')
    init_model(settings)

    # Add design docs to CouchDB.
    path = sys.path[0] + '/_design'
    print('loading views at %s' % path)
    loader = FileSystemDocsLoader(path)
    loader.sync(Session.auth)

    # Add a user, group, and permission to CouchDB.
    user_name = 'admin'
    user_password = 'password'
    group_name = 'administrators'
    perm_name = 'superpowers'

    print('loading data')
    perm = Permission(name=perm_name)
    perm.save()
    group = Group(name=group_name)
    group.permissions.append(perm)
    group.save()
    user = User.create(user_name, user_password)
    user.groups.append(group)
    user.save()

def main(argv=sys.argv):
    dist = pkg_resources.get_distribution('pyramid_couchauth_example')
    root = dist.location
    config = 'config:' + os.path.join(root, 'development.ini')
    settings = appconfig(config, 'pyramid_couchauth_example')
    setup_app(settings)

if __name__ == '__main__':
    main()

