import requests, json



response = requests.get('http://ergast.com/api/f1/current/constructorStandings.json') 
prin = response.json()
print(prin)
