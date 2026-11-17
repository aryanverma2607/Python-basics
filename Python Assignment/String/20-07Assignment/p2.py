'''
2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started

'''
string=input("Input :").split()
i=0
j=0
word=""
while i<=len(string):
	ch=string[i]
	while j>=i:
		if ch==string[j]:
			pass
		else:
			word=word+" "+ch
			break
		j+=1
	i+=1
print(word)
