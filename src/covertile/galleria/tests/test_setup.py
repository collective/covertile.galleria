# -*- coding: utf-8 -*-
from covertile.galleria.config import PROJECTNAME
from covertile.galleria.interfaces import IBrowserLayer
from covertile.galleria.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers

import unittest


class InstallTestCase(unittest.TestCase):

    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        self.assertTrue(self.qi.isProductInstalled('collective.js.galleria'))

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())


class UninstallTestCase(unittest.TestCase):

    """Ensure product is properly removed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browser_layer_removed(self):
        self.assertNotIn(IBrowserLayer, registered_layers())

    @unittest.expectedFailure  # FIXME: remove tiles on uninstall
    def test_tile_removed(self):
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        tiles = registry['plone.app.tiles']
        self.assertNotIn(u'collective.cover.carousel', tiles)
