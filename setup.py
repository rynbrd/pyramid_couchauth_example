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

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = ['pyramid',
    'WebError',
    'pyramid_couchauth',
    'py_bcrypt']

setup(name='pyramid_couchauth_example',
      version='0.0',
      description='Working pyramid_couchauth example.',
      long_description='A full pyramid project implementing pyramid_couchauth as the authentication/authorization mechanism.',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
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
      paster_plugins=['pyramid'],
      )

