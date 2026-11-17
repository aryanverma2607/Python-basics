
A
AB
ABC
ABCD
ABCDE

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		a=chr(64+j)
		print(a,end=" ")
		j=j+1
	print()
	i=i+1