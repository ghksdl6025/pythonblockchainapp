import bson
import json
with open('./output.json','r') as f:
    content = f.read()
    data = json.loads(content)
print(len(data))