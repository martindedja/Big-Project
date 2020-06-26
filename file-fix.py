import requests
import json
import hashlib
from bs4 import BeautifulSoup

"""
CUSTOM API FOR TEMPMAIL (https://temp-mail.org/)
You need an account at https://rapidapi.com/
"""

class TempMailApi():

	api_key = "0d18b41961msh686fa5e32941c91p16cfbfjsnd36649814485"

	def mailtoMD5(self,email):
	    m = hashlib.md5()
	    m.update(email.encode('utf-8'))
	    return m.hexdigest()

	def mailInbox(self,email):

		mail_md5 = self.mailtoMD5(email)
		url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/"+mail_md5+"/"

		headers = {
		    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
		    'x-rapidapi-key': "0d18b41961msh686fa5e32941c91p16cfbfjsnd36649814485",
		    }

		response = requests.request("GET", url, headers=headers)

		data = json.loads(response.text)
		data = data
		for mails in data:
			mail_html = mails['mail_html']
			soup = BeautifulSoup(mail_html, features="lxml")
			for a in soup.find_all('a', href=True):
				url_link = a['href']
				print("[+] Opening link: {}".format(url_link))
				if self.openLink(url_link) == True:
					print("[+] Email was verified successfully")

	def openLink(self,link):

		url = link
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		response = requests.request("GET", url, headers=headers)

		if response.status_code == 200:
			return True


tempMail = TempMailApi()
tempMail.mailInbox("test@sweatmail.com")
