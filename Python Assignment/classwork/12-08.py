'''
from collections import namedtuple
student=namedtuple("Student",["name","age","city"])

s1=student("Aryan",22,"Madhya pradesh")

Account=namedtuple("account",["accno","accholdername","balance"])

accno=int(input("enter Account number"))
name=input("Enter name :")
bal=float(input("Enter balance :"))


acc=Account(accno,name,bal)
print("Account Detail")
print(acc.accno)
print(acc.accholdername)
print(acc.balance)
'''
'''
from collections import namedtuple  # module
Student=namedtuple("Student",["rollno","name","marks"])   # structure of namedtuple
N=int(input("Enter number of student : ")) # number of student
students=[]  # empty list
for i in range(N):   # loop number of student ke time chalega
	print("Enter details")  # details read karwaenge
	r=int(input("Enter roll no. :"))
	name=input("Enter name :")
	m=float(input("Enter marks :"))
	S=Student(r,name,m)    #details lene ke bad Objest banaenge namedtuple ka
	students.append(S)   # object ko empty list mein append karwaenge details store karne ke liye
print()
print("details")
for i in students:
	print(i)  # ye field ke according data display karega
	print(i.name," and ",i.marks)  #i field ke name se aaega 

'''
from collections import namedtuple
product=namedtuple("ProductDetail",["name","price","Quantity"])

K=int(input("Enter number of product : "))

print()
productlist=[]
for i in range(K):
	print("Enter Details : ")
	pname=input("Enter Product name : ")
	price=float(input("Enter Product Pice : "))
	quantity=int(input("Enter Product Quantity : "))
	p=product(pname,price,quantity)
	productlist.append(p)
for i in productlist:
	print(i)
	



