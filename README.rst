******************
covertile.galleria
******************

.. contents::

Life, the Universe, and Everything
----------------------------------

A carousel tile for collective.cover based on the `Galleria`_ JavaScript image gallery framework.

.. _`Galleria`: http://galleria.io/

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/covertile.galleria.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/covertile.galleria

.. image:: https://coveralls.io/repos/collective/covertile.galleria/badge.png
    :alt: Coveralls badge
    :target: https://coveralls.io/r/collective/covertile.galleria?branch=master

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/covertile.galleria/issues

Don't Panic
-----------

Installation
^^^^^^^^^^^^

To enable this product in a buildout-based installation:

1. Edit your buildout.cfg and add ``covertile.galleria`` to the list of eggs to
   install ::

    [buildout]
    ...
    eggs =
        covertile.galleria

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to `covertile.galleria`` and click the 'Activate' button.

Usage
^^^^^

A carousel tile shows a slideshow made with a list of individual items;
every item will show an image, title and description.

You can drop any object into a carousel tile,
and you can remove and reorder them.
You can also specify if the carousel will start playing the slideshow automatically or not.
Every item in the slideshow will have a link pointing back to the original object.

Carousel tiles are fully responsive,
so be sure to configure it to use the image size that fits better the maximum desired size.
They also support native-like swipe movements and use hardware optimized animations.
