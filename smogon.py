import requests
import re
import json

response = requests.get('https://www.smogon.com/dex/ss/pokemon/')

data = "".join(re.findall(r'dexSettings = (\{.*\})', response.text))
data = json.loads(data)
data = data.get('injectRpcs', [])[1][1].get('pokemon', [])

f = open("pokemon.csv", "a")
f.write(str("Pokemon,Format\n"))

for row in data:
  name   = row.get('name', '')
  format = ""
  if(len(row.get('formats', '')) > 0):
    format = row.get('formats', '')[0]
	
  f.write(str(name+","+format+"\n"))
f.close()