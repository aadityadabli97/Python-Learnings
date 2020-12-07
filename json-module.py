
import json

data = '{"var1":"harry", "var2":56}'
print(data['var1']) #its a string can give var1 value

parsed = json.loads(data)
print(parsed['var1'])
print(type(parsed))

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

