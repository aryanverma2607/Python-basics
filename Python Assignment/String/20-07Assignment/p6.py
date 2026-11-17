'''
6. AI Chat Toxic Pattern Detector
An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.
If found:
text
Spam Pattern Found
Else:
text
Clean Message

### Input:
text
heyyy broooo welcome

### Output:
text
Spam Pattern Found
'''
string=input("Input : ")
word=""
alpha=""
for i in string:
	if "z">=i>="a" or "Z">=i>="A":
		alpha=alpha+i
	elif i==" ":
		alpha=alpha+i
	else:
		alpha=alpha
i=0
while i<len(alpha):
	if i+1<len(alpha):
		if alpha[i]==alpha[i+1]:
			word=word
		else:
			word=word+alpha[i]
	i+=1
if word!="":
	word=word+alpha[-1]	
print(word)