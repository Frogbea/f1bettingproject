import requests, json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get('http://ergast.com/api/f1/current/constructorStandings.json') 
print(response.status_code)
jprint(response.json())

print('hello world')
print('hello')