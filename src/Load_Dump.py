# load() and dump() are functions from Python's json module that are used to work with JSON data.

# dump() → Writes Python data into a JSON file.
# load() → Reads JSON data from a file and converts it into Python objects.

#dump() : Write Python Data to JSON File

# Python → JSON File
import json

student = {
    "name": "Hiloni",
    "age": 23,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("Data saved successfully.")

#load() : Read JSON File
# JSON File → Python

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
print(data["age"])
print(data["course"])

# Note:

# json.dumps()	json	Python → JSON String
# json.loads()	json	JSON String → Python
# pickle.dump()	pickle	Python → Binary File
# pickle.load()	pickle	Binary File → Python