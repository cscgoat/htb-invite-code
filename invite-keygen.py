#!/usr/bin/python3

import requests, json, base64

rtxt = requests.post("https://www.hackthebox.eu/api/invite/generate").text
code = base64.b64decode(json.loads(rtxt)['data']['code']).decode('latin-1')
print(code)
