import plone.api
from Products.Five.browser import BrowserView

from ..content.dynaperson import ORGANIZATIONS_VOCABULARY
from ..content.dynaperson import KEYWORDS_VOCABULARY
from ..content.dynaperson import NUMBER_TYPE_VOCABULARY


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
                        number_type_str=NUMBER_TYPE_VOCABULARY.getTerm(number_type).title,
                        number=format_number(**d)))

        return result

    def get_keywords(self):
        return [KEYWORDS_VOCABULARY.getTerm(kw).title for kw in self.context.keywords]

    def get_organizations(self):
        return [ORGANIZATIONS_VOCABULARY.getTerm(org).title for org in self.context.organizations]
