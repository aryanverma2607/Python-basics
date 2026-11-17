#70. Compare the number of times 'the' and 'is' appear.

string=input("Enter string: ")


'''
print("the:",string.count("the"),"is:",string.count("is"))
'''




words=string.split()

count=0
count1=0
for i in words:
	if i=="the":
		count+=1
	if i=="is":
		count1+=1
print("The:",count,"Is:",count1)