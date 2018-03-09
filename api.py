import requests
import base64


headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}
data = {
    'site_id': 'plone',
    'extension_ids': [],
#    'extension_ids': ['plonetheme.barceloneta:default', 'dynamore.policy:default'],
}

auth = ('admin', 'admin')
url = 'http://localhost:6080/recreate-plone-site'
result = requests.post(
    url,
    auth=auth,
    headers=headers,
    json=data)

print result
