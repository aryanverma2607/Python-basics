								'''
     1
    10
   101
  1010
 10101
101010
'''
n=int(input("Enter number = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=1
	while s<=i:
		if s%2==0:
			print("0",end=" ")
		else:
			print("1",end=" ")
		s=s+1
	print()
	i=i+1
