'''
9.Bike Service Kilometer Checker
A bike needs service every 3000 km.
Write a program to:
- Read travelled kilometers
- Print every service checkpoint till entered km
Input:
10000
Output:
3000 6000 9000
'''

n=int(input("Enter Number = "))
i=1
while n>=i:
	p=3000*i
	if p>n:
		break	
	print(p,end=" ")
	i=i+1

'''
If n<3000
    Ni servise 
Else: 
    i = 3000
    While i<=n:
         If i%3000: 
              Print (i)
         I+=3000

n=int(input("Enter Number = "))
i=3000
if n<3000: 
	print("No servise") 
else: 
	i = 3000
	While n>=i:
		If i%3000: 
			Print (i)
			i+=3000
'''

