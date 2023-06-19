import json
import os
absolute_path = os.path.dirname(os.path.abspath(__file__))

with open(absolute_path+"\data.json", 'r') as f:
    json_data = f.read()

data = json.loads(json_data)
for i in data:
    print(f"{i['id']}.{i['name']} - {i['professional']} - {i['country']}")
