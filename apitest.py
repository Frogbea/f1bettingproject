import requests, json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get('http://ergast.com/api/f1/current') 
print = jprint(response.json())
