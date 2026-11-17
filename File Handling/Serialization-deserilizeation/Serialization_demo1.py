import pickle

# Serialization = it is the process of storing python  object into a file
# Uses: 1. so it can be sent over a network
# 2. python object can't sent across network
# it is sent through files for which serialization is required to store python object
# 3. to save object in database they do not understand python object 
# so they store object as a text so serialization is required
student={'id':101,'name':"Aryan",'Course':'Python'}

file=open("student.txt","wb")
pickle.dump(student,file)
file.close()
print("Object Serilized Successfully")

with open("student.txt",'rb') as file:
    result = pickle.load(file)
print(result)
print("Done")