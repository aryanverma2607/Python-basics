'''
    *
   **
  ***
 ****
*****
'''
n=int(input("Enter Number = "))
i=1
while i<=n: 
	j=n
	while j>i:
		print(" ",end=" ")
		j=j-1
	a=1
	while a<=i:
		print("*",end=" ")
		a=a+1
	print()
	i=i+1	 
