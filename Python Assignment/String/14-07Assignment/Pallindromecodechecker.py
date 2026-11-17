'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''
'''
code=input("Enter Product Code = ")
i=-1
rev=""
c=-len(code)
while i>=c:
	rev=rev+code[i]
	i=i-1
if rev==code:
	print("Palindrom Code")
else:
	print("Not a Palindrome Code")
	
'''
