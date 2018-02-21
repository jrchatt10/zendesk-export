import requests
import json

credentials = 'customercare@invincea.com', 'f[0*SfM0>2m^~3p'
session = requests.Session()
session.auth = credentials
zendesk = 'https://invinceasb.zendesk.com'

#Get User List with no Org
with open('user_data_no_org.txt', 'w', encoding='utf8') as outfile:
	url_users = zendesk + '/api/v2/users.json'
	response_users = session.get(url_users)
	data_users = response_users.json()
	users = data_users['users']
	json.dump(users, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
