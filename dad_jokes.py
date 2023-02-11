import requests, json
from replit import db

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 

joke = result.json()

jk = joke["joke"]
id = joke["id"]
print(jk)
def save():
  db[id]=jk
def list():
  keys = db.keys()
  for keys in db:
    print(keys)
def next():
  joke = result.json()
  print(json.dumps(joke, indent=2))


while True:
  ask = input("Do you want to save(1) the joke, list all(2) or view next one(3)")
  if ask == '1':
    save()
  elif ask == '2':
    list()
  elif ask == '3':
    next()
    