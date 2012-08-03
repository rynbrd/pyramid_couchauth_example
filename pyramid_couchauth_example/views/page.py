# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.
"""
Define page actions.
"""

from pyramid.security import authenticated_userid


def public(context, request):
    """Get public page data."""
    username = authenticated_userid(request)
    if username is None:
        username = ""
    return {'username': username}

def private(context, request):
    """Get private page data."""
    return {}

