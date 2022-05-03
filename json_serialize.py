import json 

myscr = {
        "person_name":"Vishwajeet Salunke",
        "person_address":"Osmanabad"
    }


with open("jsd.json","w") as myfile:
    json.dump(myscr,myfile,indent=4)
    

# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)
