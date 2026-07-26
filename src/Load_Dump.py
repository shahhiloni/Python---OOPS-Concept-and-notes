# load () - reads JSON Data from a file and converts it into python objects

# dump() - write python data to JSON File 


import json

student = {
    "name": "xyz", 
    "email": "xyz@gmail.com", 
    "course": "python"
}

with open("studentss.json", "w") as file:
    json.dump(student, file)


with open("studentss.json", "r") as file:
   xxx = json.load(file)

#    json.load(file ) = value 
print("data insert successfully")





