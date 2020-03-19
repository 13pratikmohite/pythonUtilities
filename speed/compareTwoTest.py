import requests
import csv

parameters = {"lat": 40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-now.json")
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})
# https://speedcurve.com/<domain>/<domain>-us/site/?b=chrome&cs=lg&d=3&dc=1&de=1&ds=1&r=us-west-1&s=226843&u=271656
r = requests.get(
    'https://api.speedcurve.com/v1/tests/190624_DF_98e87c84e90a53f22cc553d54145363b',
    auth=('<authId>', ''))

r2 = requests.get(
    'https://api.speedcurve.com/v1/tests/190628_BA_5361081beba08ef41c47b7a2b57d5da8',
    auth=('<authID>', ''))
print(r.status_code)
#print(r.content)

data = r.json()
data2 = r2.json()
print(type(data))
print(data)

rows = zip(data, data2)
'''
with open('output.csv', "w") as f:
    writer = csv.writer(f)
    for key, value in rows:
        writer.writerow([value])
'''
with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in data.items():
        #writer.writerow([key, value])
        result = ""
        if (type(value) == int):
            print("hello")
            print(data2[key])
            result = str(value - data2[key])
        else:
            result = "null"
        writer.writerow([key, value, data2[key], result])
