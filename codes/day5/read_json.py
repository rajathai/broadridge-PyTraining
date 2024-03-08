import json

# Reading JSON data from a file
with open("example.json", "r") as file:
    data = json.load(file)

print(data)
