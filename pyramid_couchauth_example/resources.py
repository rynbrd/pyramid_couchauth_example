# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.
"""
Define additional resources.
"""

class Resource(dict):

    """Resource base class."""

    __name__ = None
    __parent__ = None

    def __init__(self, contents={}):
        """Initialize the resource."""
        dict.__init__(self, contents)
        for k, v in self.iteritems():
            self[k].__name__ = k
            self[k].__parent__ = self

    def __setitem__(self, key, item):
        """Set resource item."""
        item.__name__ = key
        item.__parent__ = self
        dict.__setitem__(key, item)


class Root(Resource):
    """Root resource."""


class Auth(Resource):
    """Auth resource."""


class Page(Resource):
    """Page resource."""


def get_root(request):
    """Get root resource."""
    return Root({
        'auth': Auth(),
        'page': Page()})

