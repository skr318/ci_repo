import requests
import json


url = "https://sanjev.supporthive.com/api/v2/staff-login/"
username = "sanjev.k@happyfox.com"
password = "Qwert12345!"
payload = {
	"username":username,
	"password":password
	}

def test_staff_auth():
	staff_login = requests.request("POST", url, data = payload).text.encode('utf8')
	staff_login_dict = json.loads(staff_login)
	staff_auth = staff_login_dict['auth_token']
	assert len(staff_auth) > 0
	assert staff_login.status_code == 200
