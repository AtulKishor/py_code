import requests, json

cm = requests.get('https://bored-api.appbrewery.com/random')

obj = json.loads(cm.text)
print(type(obj))

print(type(cm.text))
print(len(cm.text),len(json.dumps(obj)))

print('headers',json.dumps(dict(cm.headers), indent=2))