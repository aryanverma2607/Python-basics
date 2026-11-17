'''
654321
 54321
  4321
   321
    21
     1
'''
n=int(input("Enter Number = "))
i=n
while 1<=i:
	s=n
	while s>i:
		print(" ",end=" ")
		s=s-1
	j=i
	while j>=1:
		print(j,end=" ")
		j=j-1
	print()
	i=i-1