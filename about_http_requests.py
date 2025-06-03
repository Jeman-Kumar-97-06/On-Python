import requests

#Making a get request and printing the response:
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if (response.status_code==200):
    print(response.json())
else:
    print(f"Error : {response.status_code}")

#Making a POST request:
response = requests.post('https://jsonplaceholder.typicode.com/posts',{"title":"Batman vs Joken"})

if (response.status_code==201):
    print(response.json())
else:
    print(f"Error : {response.json()}")