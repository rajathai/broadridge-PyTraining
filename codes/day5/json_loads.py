json_string = '{"name": "Rajath Kumar", "age": 31, "cities_visited": ["Paris", "London", "Dubai"]}'

import json

parsed_data = json.loads(json_string)

print(parsed_data)

data = json.dumps(json_string, indent=4)
print(data)
