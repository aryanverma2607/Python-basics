n=int(input("Enter Number: "))

while n>0:
	r=n%10
	n=n//10
print(r)


'''
a=len(str(n))
print(n//((10)**(a-1)))

'''
for i in range(1,len(str(n))+1):
	r=n%10
	n=n//10
print(r)
'''