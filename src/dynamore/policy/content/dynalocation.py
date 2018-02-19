# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from dynamore.policy import _
from .dynaperson import IContactRow
from .dynaperson import ORGANIZATIONS_VOCABULARY


class IDynalocation(model.Schema):
    """ Marker interfce and Dexterity Python Schema for Dynalocation
    """

    short_title = schema.TextLine(
        title=_(u'Short title'),
        required=False
    )
    address1 = schema.TextLine(
        title=_(u'Address 1'),
        required=False
    )
    address2 = schema.TextLine(
        title=_(u'Address 2'),
        required=False
    )
    address3 = schema.TextLine(
        title=_(u'ZIP code/city'),
        required=False
    )
    address4 = schema.TextLine(
        title=_(u'Country'),
        required=False
    )

    directives.widget(organizations=CheckBoxFieldWidget)
    organizations = schema.List(
        title=_('Organizations'),
        description=_('Organizations'),
        required=True,
        value_type=schema.Choice(source=ORGANIZATIONS_VOCABULARY),
    )

    directives.widget(contacts=DataGridFieldFactory)
    contacts = schema.List(
        title=_(u'Contacts'),
        required=False,
        value_type=DictRow(
            title=_(u'Contacts'), 
            schema=IContactRow))


@implementer(IDynalocation)
class Dynalocation(Item):
    """
    """
