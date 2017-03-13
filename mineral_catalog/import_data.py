import json

count = 0
output = []
with open('minerals.json') as mineralfile:
    minerals = json.load(mineralfile)
    for mineral in minerals:
        data = {
            "model": "minerals.mineral",
            "pk": count + 1,
            "fields": {k.replace(' ', '_'): v
                for k, v in minerals[count].items()}}
        output.append(data)
        count += 1

with open('ammended.json', mode='w', encoding='utf-8') as f:
    json.dump(output, f)
