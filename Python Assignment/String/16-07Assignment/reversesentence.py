'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP
'''
'''
REVERSE INDEXING

s=input("Input = ")
i=len(s)-1
r=""
while i>=0:
	r=r+s[i]
	i=i-1
print(r,end="")

'''
'''
SLCING CONCEPT

s=input("Input = ")
i=len(s)-1
while i>=0:
	print(s[i][::-1],end="")
	i=i-1
'''
'''
WHILE LOOP

s=input("Input = ")
i=0
rev=""
print()
while i<len(s):
	a=s[i]
	rev=a+rev
	i=i+1
print(rev,end="")
'''
'''
#FOR LOOP

s=input("Input = ")
rev=""
for i in range(len(s)-1,-1,-1):
	ch=s[i]
	rev=rev+ch
print(rev)
'''



