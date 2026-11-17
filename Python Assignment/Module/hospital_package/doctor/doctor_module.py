def add_doctor():
    d={}
    d["id"]=input("Enter Doctor ID:")
    d["name"]=input("Enter Doctor name:")
    d["specialization"]=input("Enter your Specification:")
    d["experience"]=int(input("Enter your experience:"))
    d["fee"]=int(input("Enter Cunsultation fees:"))
    return d

def display_doctors(n):
    for i in range(len(n)):
        for i,k in n[i].items():
            print(i,":",k)
        print()
