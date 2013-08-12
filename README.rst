CMSplugin Video Gallery
=======================

A reusable Django app to display video plugins in placeholders or a video
gallery with cms apphook.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install cmsplugin-video-gallery

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/bitmazk/cmsplugin-video-gallery.git#egg=video_gallery

TODO: Describe further installation steps (edit / remove the examples below):

Add ``video_gallery`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'video_gallery',
    )

Add the ``video_gallery`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^videos/', include('video_gallery.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate video_gallery


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-video-gallery
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
