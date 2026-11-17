print("Average marks counter")
num1,num2,num3=map(int,input("Enter numbers of three subjects separated by '-':").split("-"))
marks=(num1+num2+num3)//3
print(F"Average of marks is {marks}")