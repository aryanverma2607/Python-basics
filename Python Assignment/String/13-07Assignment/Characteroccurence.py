'''
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o
'''


s=input("Enter Product Review = ")
ch=input("Enter character = ")
count=0
i=0
while i<len(s):
	if s[i]==ch:
		count=count+1
	i=i+1
print(count)
'''

s=input("Enter Product Review = ")
ch=input("Enter character = ")
print(s.count(ch))
'''