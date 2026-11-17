import pickle

# Desirealization = converting stremas of bytes back into object of python program/
# original object of python program
with open("student.txt","rb") as f:
    result = pickle.load(f)
print(result)

import json