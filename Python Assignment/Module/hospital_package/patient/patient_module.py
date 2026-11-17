def add_patient():
    d={}
    d["id"]=input("Enter patient id:")
    d["name"]=input("Enter Patient name:")
    d["age"]=int(input("Enter patient age:"))
    d["gender"]=input("Enter gender:")
    d["disease"]=input("Enter disease name:")
    d["p_number"]=int(input("Enter Phone number:"))
    return d

def display_patients(n):
    for i in range(len(n)):
        for k,v in n[i].items():
            print(k,":",v)
        print()

def search_patients(n):
    id=input("Enter Patient id:")
    for i in range(len(n)):
        for k,v in n[i].items():
            if k=="id" and v==id:
                print("Patient Found")
                for k,v in n[i].items():
                    print(k,":",v)
                break
        else:
            print("Patient Not found")