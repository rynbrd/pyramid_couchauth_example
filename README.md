Pyramid CouchDB Auth Example
============================

[Pyramid][1] project implementing [pyramid_couchauth][2].

Running the Example
-------------------

CouchDB will need to be running locally and contain an empty database named
"auth".

Retrieve the source code:

```
git clone --depth 1 git:://github.com/BlueDragonX/pyramid_couchauth_example.git
```

Load the example data into the database:

```
cd pyramid_couchauth_example
python init.py
```

Service the project with paster:

```
paster serve development.ini
```

Paster will inform you where it's hosting the project. Opening the site in a
browser will show you the default Pyramid example page. Move to /page and it
will show you the publicly accessible page and provide some basic few
navigational links.

[1]: http://pylonsproject.org/							"Pyramid"
[2]: https://github.com/BlueDragonX/pyramid_couchauth/	"pyramid_couchauth"
