import json

student={"Name":"Kunal","Age":21,"Is_Active":True}

# dumps/loads works only on RAM
# serialize to a json string
insert = json.dumps(student)

# deserialize back to a python dictionary
load = json.loads(insert)



# dump/load directly work on hard drive
# Serialize to file
with open("data_json.txt",'w') as file:
    json.dump(student,file,indent=4)


# deserialize from a file
with open("data_json.txt","r") as file:
    json.load(file)
print(load)