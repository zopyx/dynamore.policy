import plone.api
from Products.Five.browser import BrowserView


def format_number(number_type, country_code, area_code, number):
    """ Format a phone number """
    return u'+{0} {1} {2}'.format(country_code, area_code, number)


class Dynaperson(BrowserView):

    def get_contacts(self):
        """ Return contacts formatted """

        result = list()
        for number_type in ('phone', 'mobile', 'fax'):
            for d in self.context.contacts:
                if d['number_type'] == number_type:
                    result.append(dict(
                        number_type=number_type,
                        number=format_number(**d)))

        return result
