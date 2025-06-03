import http.client
import json

conn    = http.client.HTTPSConnection('jsonplaceholder.typicode.com')
headers = {"Content-type":"application/json"}
payload = json.dumps({"username":"john",'passw':'Jack'})

conn.request('POST','/posts',body=payload,headers=headers)
response = conn.getresponse()
data     = response.read()
print(data.decode('utf-8'))
print(data)