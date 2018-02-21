import requests
import json

credentials = 'customercare@invincea.com', 'f[0*SfM0>2m^~3p'
session = requests.Session()
session.auth = credentials
zendesk = 'https://invinceasb.zendesk.com'

#Export all Ticket Data and Ticket Comments
ticket_min = 1
ticket_max = 50

while ticket_max =! 1555:
	with open('ticket_data_' + str(ticket_min) + '-' + str(ticket_max) + '.txt', 'w', encoding='utf8') as outfile:
		for tix_id in range(ticket_min, ticket_max + 1):
			url_tix = zendesk + '/api/v2/tickets/' + str(tix_id) + '.json'
			url_cmt = zendesk + '/api/v2/tickets/' + str(tix_id) + '/comments.json'
			response_tix = session.get(url_tix)
			response_cmt = session.get(url_cmt)
			if response_tix.status_code != 200:
				continue
			if response_cmt.status_code != 200:
				continue
			data_tix = response_tix.json()
			tix = data_tix['ticket']
			data_cmt = response_cmt.json()
			cmt = data_cmt['comments']
			outfile.write(str(tix_id)+"\n")
			json.dump(tix, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
			json.dump(cmt, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
			outfile.write("\n")
	ticket_min = ticket_min + 50
	if ticket_max < 1550:
		ticket_max = ticket_max + 50
	elif ticket_max = 1550:
		ticket_max = 1554
	else:
		ticket_max = 1555
