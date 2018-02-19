import plone.api
from Products.Five.browser import BrowserView

class Richfolder(BrowserView):


    @property
    def catalog(self):
        return plone.api.portal.get_tool('portal_catalog')

    def entries(self):

        query = {
                'portal_type': 'richfolder',
                'path' : {'depth': 1, 'query': '/'.join(self.context.getPhysicalPath())}
                }

        brains = self.catalog(**query)
        for brain in brains:
            yield brain.getObject()
