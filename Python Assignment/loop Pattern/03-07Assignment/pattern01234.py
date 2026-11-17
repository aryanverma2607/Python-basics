'''
0
01
012
0123
01234
'''
n=int(input("Enter Number = "))
i=0
while i<n:
	j=0
	while j<=i:
		print(j,end=" ")
		j=j+1
	print()
	i=i+1