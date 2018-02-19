# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.directives import form
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope.schema.vocabulary import SimpleVocabulary
from zope import schema
from zope.interface import implementer
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from dynamore.policy import _


KEYWORDS = [
    'ANSA',
    'Administration',
    'Beratung IT-Konzepte',
    'Bestellabwicklung',
    'Biomechanik',
    'Branch Manager Dresden',
    'Branch Manager Ingolstadt',
    'Business Manager DYNAmore France SAS',
    'Business Manager DYNAmore Italia S.r.l.',
    'Business Manager DYNAmore Swiss GmbH',
    'CAE Integration',
    'CAE-Prozesse',
    'Cluster Technologie',
    'Compliance',
    'Director DYNAmore Nordic AB',
    'Dummymodelle',
    'Einsatz LS-DYNA',
    'Erstkontakt',
    'FE Technologie',
    'FE-Models',
    'FEM-Methoden',
    'FEMZIP',
    'Finance',
    'Foam and Plastic',
    'Forming Technology',
    'HPC',
    'Implicit',
    'Insassenschutz',
    'Insassensicherheit',
    'Key Account',
    'Kundensupport DYNAmore France SAS',
    'LS-DYNA',
    'LS-DYNA Development',
    'LS-OPT',
    'LS-OPT Development',
    'LS-PrePost Development',
    'Lizenzierung',
    'LoCo',
    'Loco2',
    'Marketing',
    'Material modeling',
    'Materialgesetze',
    'Menschmodelle',
    'Modell-Entwicklung',
    'Modelle',
    'Multiphysik',
    'Optimierung',
    'Personal',
    'Primer',
    'Projektabrechnung',
    'Projekte',
    'Prozesssimulation',
    'Rechnungswesen',
    'Sales Coordinator',
    'Sales Software',
    'Schulungen',
    'Seminarorganisation',
    'Sitzentwicklung',
    'Software Sales',
    'Status.E',
    'StatusE',
    'Support',
    'Support CAViT',
    'Support LoCo',
    'Training',
    'Umformsimulation',
    'Umformtechnik',
    'Vertrieb',
    'Vertrieb DYNAFORM',
    'Verwaltung',
    'eta/Dynaform',
    'mETA'
]


KEYWORDS_VOCABULARY = SimpleVocabulary.fromValues(KEYWORDS)

NUMBER_TYPE_VOCABULARY = SimpleVocabulary.fromValues([u'phone', u'mobile', u'fax'])

ORGANIZATION_VOCABULARY = SimpleVocabulary.fromValues([u'default', u'scale', u'dynamore-ch'])


class IContactRow(form.Schema):

    number_type = schema.Choice(
        title=_(u'Number type'),
        required=True,
        vocabulary=NUMBER_TYPE_VOCABULARY
    )

    country_code = schema.TextLine(
        title=_(u'Country code'),
        required=True
    )

    area_code = schema.TextLine(
        title=_(u'Area code'),
        required=True
    )

    number = schema.TextLine(
        title=_(u'Number'),
        required=True
    )



class IDynaperson(model.Schema):
    """ Marker interface and Dexterity Python Schema for Dynaperson
    """

    firstname = schema.TextLine(
        title=_(u'Firstname'),
        required=True
    )
    lastname = schema.TextLine(
        title=_(u'Firstname'),
        required=True
    )
    email = schema.TextLine(
        title=_(u'Email'),
        required=True
    )

    directives.widget(organization=CheckBoxFieldWidget)
    organization = schema.List(
        title=_('Organization'),
        description=_('Organization'),
        required=True,
        value_type=schema.Choice(source=ORGANIZATION_VOCABULARY),
    )

    directives.widget(keywords=CheckBoxFieldWidget)
    keywords = schema.List(
        title=_('Roles'),
        description=_('Roles'),
        required=False,
        value_type=schema.Choice(source=KEYWORDS_VOCABULARY),
    )

    directives.widget(contacts=DataGridFieldFactory)
    contacts = schema.List(
        title=_(u'Contacts'),
        value_type=DictRow(
            title=_(u'Contacts'), 
            schema=IContactRow))



@implementer(IDynaperson)
class Dynaperson(Item):
    """ """
