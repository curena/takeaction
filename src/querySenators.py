import urllib.request
import config
import json

state = "TX"

url = "https://api.propublica.org/congress/v1/members/senate/" + state + "/current.json"

req = urllib.request.Request(url, headers = config.headers)
resp = urllib.request.urlopen(req)
data = resp.read()

#data = data.decode("utf-8")
data = json.loads(data)

print(state + " senators are " + data['results'][0]['name'] + " and " + data['results'][1]['name'] + ".")

print(type(data))