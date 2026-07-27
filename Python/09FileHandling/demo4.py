import json

# data = {
#     "name": "Ayush",
#     "age": 30,
#     "city": "New York"
# }

# json_data = json.dumps(data)
# print(type(data))
# print(type(json_data))
# print(json_data)



# Deserialization

json_data = '{"name": "Ayush", "age": 30, "city": "New York"}'

data = json.loads(json_data)
print(data)
print(type(data))
print(data["name"])
print(data["age"])