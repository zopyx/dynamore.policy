
import json
from Products.Five.browser import BrowserView
from Products.CMFPlone.factory import addPloneSite
import zExceptions


class API(BrowserView):

    def recreate_plone_site(self):
        """ Recreate a Plone site """

        data = json.loads(self.request.BODY)
        site_id = str(data['site_id'])
        extension_ids = data['extension_ids']

        root = self.context.restrictedTraverse('/')
        if site_id in root.objectIds():
            print 'Deleting Plone site "{0}"'.format(site_id)
            root.manage_delObjects([site_id])

        print 'Creating Plone site "{0}" with {1}'.format(site_id, extension_ids)
        addPloneSite(root, site_id, extension_ids=extension_ids)
        print 'Created Plone site "{0}" with {1}'.format(site_id, extension_ids)

        self.request.response.setStatus(201)
        self.request.response.write('Created')


    def remote_exists(self, path):
        """ Check if `path` exists based on our own traversal.
            The purpose of this method is to provide a traversal
            lookup that is not dependent on Acquisition but on
            real traversal.
            E.g. a request to `/plone/papers/conference/papers` would
            resolve to the first `papers` folder if the second 
            `papers` folder does not exist.
        """
        current = self.context.restrictedTraverse('/')
        for c in path.split('/'):
            if not c:
                continue
            if c in current.objectIds():
                current = current[c]
            else:
                raise zExceptions.NotFound(path)
        self.request.response.setStatus(200)
        self.request.response.write('FOUND')
