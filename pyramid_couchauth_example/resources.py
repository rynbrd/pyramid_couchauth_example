# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.

class Resource(dict):
    __name__ = None
    __parent__ = None

    def __init__(self, contents={}):
        dict.__init__(self, contents)
        for k, v in self.iteritems():
            self[k].__name__ = k
            self[k].__parent__ = self

    def __setitem__(self, key, item):
        item.__name__ = key
        item.__parent__ = self
        dict.__setitem__(key, item)

class Root(Resource):
    pass

class Auth(Resource):
    pass

class Page(Resource):
    pass

def get_root(request):
    return Root({
        'auth': Auth(),
        'page': Page()})

