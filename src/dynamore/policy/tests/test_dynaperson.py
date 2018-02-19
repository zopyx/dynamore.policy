# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from dynamore.policy.content.dynaperson import IDynaperson
from dynamore.policy.testing import DYNAMORE_POLICY_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class DynapersonIntegrationTest(unittest.TestCase):

    layer = DYNAMORE_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='dynaperson')
        schema = fti.lookupSchema()
        self.assertEqual(IDynaperson, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='dynaperson')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='dynaperson')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IDynaperson.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='dynaperson',
            id='dynaperson',
        )
        self.assertTrue(IDynaperson.providedBy(obj))
