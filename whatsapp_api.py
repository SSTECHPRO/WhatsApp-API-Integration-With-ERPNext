# Copyright (c) 2022, ts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import http.client
import json

class WhatsappAPI(Document):
	def validate(self):
		conn = http.client.HTTPSConnection("api.interakt.ai")
		payload = json.dumps({
		"countryCode": "+91",
		"phoneNumber": "9940941959",
		"callbackData": "some text here",
		"type": "Template",
		"template": {
			"name": "expo_lead",
			"languageCode": "en",
			"headerValues": [
			"https://www.africau.edu/images/default/sample.pdf"
			],
			"fileName": "file_name.pdf",
			"bodyValues": [
			 self.name1
			]
		}
		})
		headers = {
		'Authorization': 'Basic Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=',
		'Content-Type': 'application/json'
		}
		conn.request("POST", "/v1/public/message/", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))



