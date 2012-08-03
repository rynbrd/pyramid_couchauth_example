# Copyright (c) 2011-2012 Ryan Bourgeois <bluedragonx@gmail.com>
#
# This project is free software according to the BSD-modified license. Refer to
# the LICENSE file for complete details.

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = ['pyramid',
    'WebError',
    'pyramid_couchauth',
    'py_bcrypt']

setup(name='pyramid_couchauth_example',
      version='0.1',
      description='Working pyramid_couchauth example.',
      long_description='A full pyramid project implementing pyramid_couchauth as the authentication/authorization mechanism.',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Ryan Bourgeois',
      author_email='bluedragonx@gmail.com',
      url='https://github.com/BlueDragonX/pyramid_couchauth_example',
      keywords='web pyramid pylons couchdb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_couchauth_example",
      entry_points = """\
      [paste.app_factory]
      main = pyramid_couchauth_example:main
      """,
      )

