import plone.api
from Products.Five.browser import BrowserView

class Richfolder(BrowserView):


    @property
    def catalog(self):
        return plone.api.portal.get_tool('portal_catalog')

    def entries(self):

        result = dict(folders=[], documents=[])
        query = {
                'path' : {'depth': 1, 'query': '/'.join(self.context.getPhysicalPath())}
                }

        brains = self.catalog(**query)
        for brain in brains:
            if brain.portal_type in ('richfolder', 'Folder'):
                result['folders'].append(brain.getObject())
            else:
                result['documents'].append(brain.getObject())
        return result
