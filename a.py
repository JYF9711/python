import http.client

conn = http.client.HTTPSConnection("binstd.apistd.com")
conn.request("POST", "/express/query?key=6sV9oo9SMWVQTenRrZYBJWyWE&type=auto&number=773058962040428")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

