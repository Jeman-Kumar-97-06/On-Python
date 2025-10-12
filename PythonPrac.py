import urllib3
http = urllib3.PoolManager()
r = http.request("GET","http://localhost:5173/home")
print(r.data)