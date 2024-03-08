import json

data = {
    "name": "Elon Musk",
    "age": 45,
    "is_employee": False,
    "skills": ["HTML", "CSS", "JavaScript"]
}

# Writing JSON data to a file
with open('new_example.json', 'w') as file:
    json.dump(data, file, indent=4)
