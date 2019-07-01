import requests
from credentials import username, password, ip
import json

url = "http://{}/ins".format(ip)
cred = (username, password)

command = {"ins_api": {"version": "1.0",
                       "type": "cli_show",
                       "chunk": "0",
                       "sid": "1",
                       "input": "sho ip int br",
                       "output_format": "json"
                       }}

HDR = {'Content-type': 'application/json',
       'Accept': 'application/json'}

resp = requests.post(url, headers=HDR, auth=cred, data=json.dumps(command))

resp_payload = resp.text
print(resp.status_code)
print(resp.text)
print(type(resp_payload))
pyobj = json.loads(resp_payload)
print(type(pyobj))
pyobj2 = resp.json()
print(pyobj == pyobj2)
