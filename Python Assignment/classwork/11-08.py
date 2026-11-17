#Multilevel nested list
'''a=[1,2,[3,4,[5,6]]]
print(a[2][2][1])
print(a[2][2][0])
print(a[1])
print(a[2][0])



#tuple
b=1,2,3,4,5

a=([1],2,3)
print(a)
#tuple creation constructor


#tuple accessing element in tuple
print(a[0])
print(a[-1])
print(a[1:2])
a[0].append(90)
print(a)


k=(10,20,30,40,50)
for value in range(len(k)):
	print(f"{value} and {k[value]}")
'''
'''
k=(10,20,30,40,50)
k2=(10,20,30,40,50)
print(id(k))
print(id(k2))

k=[10,20,30,40,50]
k2=[10,20,30,40,50]
print(id(k)) #different memory address
print(id(k2)) #different memory address
'''
'''
id=int(input("Enter Employee id : "))
name=input("Enter Name : ")
dept=input("Enter department : ")
salary=int(input("Enter Salary : "))
employee=(id,name,dept,salary)
print(employee)
print("Employee id {}".format(employee[0]))
print("Employee Name {}".format(employee[1]))
print("Employee Department {}".format(employee[2]))
print("Employee Salarty {}".format(employee[3]))


'''
name=input("Enter product name :")
price=float(input("enter product price :"))
quantity=int(input("Enter Quantity :"))
bill=(name,price,quantity)
print()

print("Total Bill = {}".format(bill[1]*bill[2]))
