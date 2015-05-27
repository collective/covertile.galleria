# -*- coding: utf-8 -*-
from collective.cover.testing import INTEGRATION_TESTING
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class VocabulariesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_available_tiles_vocabulary(self):
        name = u'collective.cover.AvailableTiles'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        tiles = vocabulary(self.portal)
        self.assertIn(u'collective.cover.carousel', tiles)

    def test_enabled_tiles_vocabulary(self):
        name = u'collective.cover.EnabledTiles'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        tiles = vocabulary(self.portal)
        self.assertIn(u'collective.cover.carousel', tiles)
