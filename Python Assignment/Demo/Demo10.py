a=input("Enter string = ")
word=a.split()
rev=""

for i in word:
	ch=i
	new=ch[::-1]
	rev=rev+new+" "
print(rev,end="")
print()
rev=""
for i in range(len(word)):
	words=word[i]
	for j in range(len(words)-1,-1,-1):
		rev=rev+words[j]+""
print(rev,end="")
print()

i=0
while i<len(word):
	ch=word[i]
	rev=""
	j=len(ch)-1
	while j>=0:
		rev=rev+ch[j]
		j-=1
	print(rev,end=" ")
	i+=1
			