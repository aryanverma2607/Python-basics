#write a program to remove all apecial character from string
'''
string=input("Enter string: ")
result=""
for i in range(len(string)):
	ch=string[i]
	if "A"<=ch<="Z" or "a"<=ch<="z" or "0"<=ch<="9":
		result=result+ch
	elif ch==" ":
		result=result+ch
print(result)
'''
#write a program to find the first non repeated character in string
'''
string=input("Enter string: ")
visited=""
for i in string:
	count=0
	if i not in visited:
		for j in string:
			if i==j:
				count=count+1
		visited=visited+i
	if count==1:
		print(i)
		break
else:
	print("Repeated Character Found")
'''
#write a program to find sortest word in a sentence
'''
string=input("Enter string: ").split()
smallest=string[0]
for i in range(1,len(string)):
	l=len(string[i])
	if len(smallest)>l:
		smallest=string[i]
print(smallest)

'''
# write a program to find tha number of unique characters in a string
'''
string=input("Enter string: ")
visited=""
uniquecount=0
print("Unique Character:",end=" ")
for i in string:
	count=0
	if i not in visited:
		for j in string:
			if i==j:
				count=count+1
		visited=visited+i
	if count==1:
		uniquecount=uniquecount+1
		print(i,end=" ")
print()
print("Total Character :",uniquecount)
'''
#write a program to find occurence of word in a string
'''
string=input("Enter string: ")
word=input("enter word: ")
c=string.count(word)
print(c)
'''
#mannually
'''
string=input("Enter string: ")
word=input("enter word: ")
count=0
i=0
while i<=len(string)-len(word):
	j=0
	match=1
	while j<len(word):
		if string[i+j]!=word[j]:
			match=0
			break
		j=j+1
	if match==1:
		count=count+1
	i=i+1
print("Total count:",count)
'''


