'''
1
00
111
0000
11111pattern
'''
n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		if i%2==0:
			print("0",end=" ")
		
		else:
			print("1",end=" ")
		j=j+1
	print()
	i=i+1