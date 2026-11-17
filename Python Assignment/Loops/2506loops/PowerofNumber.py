'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''
'''
#without loop
x=int(input("Enter number : "))
power=int(input("Enter power: "))
print(x**power)
'''
#using while loop
x=int(input("Enter number : "))
power=int(input("Enter power: "))
i=1
while i<=power:
	num=x**i
	i=i+1
print(num)
'''
#using for loop
#for i in range(1,power+1,1):
#i=1
#for i in range(power+1):
for i in range(power+1):
	num=x**i
	i=i+1
print(num)
'''