# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from dynamore.policy.content.richfolder import IRichfolder
from dynamore.policy.testing import DYNAMORE_POLICY_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class RichfolderIntegrationTest(unittest.TestCase):

    layer = DYNAMORE_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='richfolder')
        schema = fti.lookupSchema()
        self.assertEqual(IRichfolder, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='richfolder')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='richfolder')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IRichfolder.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='richfolder',
            id='richfolder',
        )
        self.assertTrue(IRichfolder.providedBy(obj))
