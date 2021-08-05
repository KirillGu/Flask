import requests, json

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'announcements/1', {'heading': 'tata', 'description': 'ratatu', 'date of creation': 10000, 'owner': 'tim'})

print(response.json())

response = requests.delete(BASE + "announcements/3")
print(response)

response = requests.get(BASE + 'announcements/1')
print(response.json())
