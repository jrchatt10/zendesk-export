import requests
import json

credentials = 'customercare@invincea.com', 'f[0*SfM0>2m^~3p'
session = requests.Session()
session.auth = credentials
zendesk = 'https://invinceasb.zendesk.com'

#Get User List From Orgs
#Get Org List
url_orgs = zendesk + '/api/v2/organizations.json'
response_orgs = session.get(url_orgs)
if response_orgs.status_code != 200:
	print('Error with status code {}'.format(response_orgs.status_code))
	exit()
data_orgs = response_orgs.json()
orgs = data_orgs['organizations']

with open('organizational_user_data.txt', 'w', encoding='utf8') as outfile:
	for org_id in orgs:
		org_id = org_id['id']
		url_user = zendesk + '/api/v2/organizations/' + str(org_id) + '/users.json'
		response_user = session.get(url_user)
		if response_user.status_code != 200:
			continue
		data_user = response_user.json()
		user = data_user['users']
		outfile.write(str(org_id)+"\n")
		json.dump(user, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
		outfile.write("\n")
