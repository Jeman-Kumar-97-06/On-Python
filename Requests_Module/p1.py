import requests
from requests.exceptions import HTTPError

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response) #This will print <Response 200> if success

print(response.status_code) # This will print 200

URLS=['https://jsonplaceholder.typicode.com/todos/2','https://jsonplaceholder.typicode.com/todos/1']

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as httperr:
        print(f'Http error occured: {httperr}')
    except Exception as err:
        print(f"Other error occurred : {err}")
    else:
        print("Success!")

print(response.content) # Response as bytes
print(type(response.content)) #<class 'bytes'>
print(response.text)    # Response as string using utf-8 as default encoding
print(type(response.text)) #<class 'str'> 
print(response.json()) #Convert the respones to a dictionary
print(response.json()['title'])

print(response.headers['Content-Type'])