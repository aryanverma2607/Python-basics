'''
3.
Reverse Sentence + Reverse Each Word(3 marks)

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
```
'''
string=input("Input : ").split()
result=""
for i in range(len(string)-1,-1,-1):
	ch=string[i]
	result=result+ch[::-1]+" "
if result[-1]==" ":
	result=result[:-1]
#print(len(result))
print(result)