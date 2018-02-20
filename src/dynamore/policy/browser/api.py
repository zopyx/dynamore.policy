from Products.Five.browser import BrowserView
import zExceptions


class API(BrowserView):

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
