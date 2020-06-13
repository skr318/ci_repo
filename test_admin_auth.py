import requests
import json
import pytest


class TestAdminAuth:
	url = "https://sanjev.supporthive.com/api/v2/staff-login/"
	username = "sanjev.k@happyfox.com"
	password = "Qwert12345!"
	payload = {
		"username":username,
		"password":password
		}
	
	
	@pytest.mark.hotfix
	def test_admin_auth(self):
		self.staff_login = requests.request("POST", self.url, data = self.payload).text.encode('utf8')
		self.staff_login_dict = json.loads(self.staff_login)
		self.staff_auth = self.staff_login_dict['auth_token']
		assert len(self.staff_auth) > 0
		assert len(self.staff_login_dict['refresh_token']) > 0
