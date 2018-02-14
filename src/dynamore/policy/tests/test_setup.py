# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from dynamore.policy.testing import DYNAMORE_POLICY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that dynamore.policy is properly installed."""

    layer = DYNAMORE_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dynamore.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'dynamore.policy'))

    def test_browserlayer(self):
        """Test that IDynamorePolicyLayer is registered."""
        from dynamore.policy.interfaces import (
            IDynamorePolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IDynamorePolicyLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DYNAMORE_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['dynamore.policy'])

    def test_product_uninstalled(self):
        """Test if dynamore.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'dynamore.policy'))

    def test_browserlayer_removed(self):
        """Test that IDynamorePolicyLayer is removed."""
        from dynamore.policy.interfaces import \
            IDynamorePolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IDynamorePolicyLayer,
           utils.registered_layers())
