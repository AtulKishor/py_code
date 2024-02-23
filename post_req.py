#post request
import requests,json
b = {"username":input("enter username"),"password":input('enter password')}
j = requests.post('https://secrets-api.appbrewery.com/register', data=b)

#get request
from http.client import HTTPSConnection
from base64 import b64encode
# Authorization token: we need to base 64 encode it
# and then decode it to acsii as python 3 stores it as a byte string
def basic_auth(username, password):
     token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
     return f'Basic {token}'
#set host
c = HTTPSConnection("secrets-api.appbrewery.com")
headers = { 'Authorization' : basic_auth(b['username'],b['password'])}
c.request('GET', '/all?page=1', headers=headers)
res = c.getresponse()
# at this point you could check the status etc
# this gets the page text
data = res.read()
data = json.loads(data.decode())#list object
print(json.dumps(data,indent=2))