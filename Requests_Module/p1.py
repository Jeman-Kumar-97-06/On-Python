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

response2 = requests.get(
    'https://api.github.com/search/repositories',
    params={"q":"language:python","sort":"stars","order":"desc"} #Sending queries
)
"""
    You can even pass the params as a tuple : 
    requests.get(
        "https://api.github.com/search/repositories",
        [("q", "language:python"), ("sort", "stars"), ("order", "desc")],
    )

    OR as a bytes:
    requests.get(
        "https://api.github.com/search/repositories",
        params=b"q=language:python&sort=stars&order=desc",
    )
"""

print("\n\n")
json_response = response2.json()
popular_repos = json_response['items']
for repo in popular_repos[:3]:
    print(f"Name:{repo['name']}")
    print(f"Description:{repo['description']}")
    print(f"Stars:{repo['stargazers_count']}\n")


response3 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q':'"real python"'},
    headers={"Accept":"application/vnd.github.text-match+json"},
)

json_response = response3.json()
first_repository = json_response['items']
print(first_repository[0]['text_matches'][0]['matches'])

"""
Sending post request with a body : 
requests.post('urlgoeshere',data={"key":"value"}) --> use data when the Content-Type u want to send is : application/x-www-form-urlencoded
requests.post('urlgoeshere',json={"key":"value"}) --> use json when the Content-Type u want to send is : JSON
"""



