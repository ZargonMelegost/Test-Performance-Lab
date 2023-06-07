
import json

with open("values.json", "r") as my_file:
    capitals_json = my_file.read()

capitals = json.loads(capitals_json)

value_dict = {}
for i in capitals["values"]:
    value_dict[i['id']] = i['value']

#----------------------------------------------------------------

with open("tests.json", "r") as my_file_2:
    struc_json = my_file_2.read()
data = json.loads(struc_json)

def update_json_value(data, values_dict):
    if isinstance(data, dict):
        if "id" in data and data["id"] in values_dict:
            data["value"] = values_dict[data["id"]]
        for key, value in data.items():
            update_json_value(value, values_dict)
    elif isinstance(data, list):
        for item in data:
            update_json_value(item, values_dict)

update_json_value(data, value_dict)
updated_json_data = json.dumps(data, indent=2)
#print(updated_json_data)
with open('report.json', 'w') as file:
    json.dump(data, file, indent=4)