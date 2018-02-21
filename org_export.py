import requests
import json

credentials = 'customercare@invincea.com', 'f[0*SfM0>2m^~3p'
session = requests.Session()
session.auth = credentials
zendesk = 'https://invinceasb.zendesk.com'

#Get Org List
with open('organization_data.txt', 'w', encoding='utf8') as outfile:
	url_orgs = zendesk + '/api/v2/organizations.json'
	response_orgs = session.get(url_orgs)
	data_orgs = response_orgs.json()
	orgs = data_orgs['organizations']
	json.dump(orgs, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

