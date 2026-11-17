'''
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d

'''


alpha=input("Input = ")
newalpha=""
visited=""
for i in range(len(alpha)):
	if alpha[i] not in visited:
		if i+1<len(alpha):
			if alpha[i]==alpha[i+1]:
				continue
			else:
				newalpha=newalpha+alpha[i]
		visited=visited+alpha[i]
if newalpha!=" ":
	newalpha=newalpha+alpha[-1]
print(newalpha)
