# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import implementer
from dynamore.policy import _


class IRichfolder(model.Schema):
    """ Marker interfce and Dexterity Python Schema for Richfolder
    """

    fieldset('Teaser', fields=[
        'teaser_title', 
        'teaser_description', 
        'teaser_text', 
        'teaser_image', 
        'teaser_image_caption'])

    text = RichText(
        title=_(u'Text'),
        required=False
    )

    teaser_title = schema.TextLine(
        title=_(u'Teaser text'),
        required=False
    )
    teaser_description = schema.Text(
        title=_(u'Teaser description'),
        required=False
    )
    teaser_text = RichText(
        title=_(u'Teaser text'),
        required=False
    )
    teaser_image = NamedBlobImage(
        title=_(u'Teaser image'),
        required=False)
    teaser_image_caption = schema.TextLine(
        title=_(u'Teaser image caption'),
        required=False)

@implementer(IRichfolder)
class Richfolder(Container):
    """
    """
