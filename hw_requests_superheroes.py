import requests

API_BASE_URL = "https://superheroapi.com/api/2619421814940190/"

superheros = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}

for name in superheros:
    response = requests.get(API_BASE_URL + f'search/{name}')
    intelligence[name] = response.json()['results'][0]['powerstats']['intelligence']

max_intel = 0
for k,v in intelligence.items():
    if int(v) > max_intel:
        max_intel = int(v)
        max_name = k

print(f'Самый умный конечно {max_name}')


