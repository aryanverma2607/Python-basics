'''
 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1
'''

string=input("Enter String :")
alpha = ""
for i in string:
	if "A"<=i<="Z":
		alpha=alpha+chr(ord(i)+32)
	elif "a"<=i<="z":
		alpha=alpha+i
	elif i==" ":
		alpha=alpha
	else:
		alpha=alpha+i
newalpha=sorted(alpha)
new="".join(newalpha)
visited=""
for i in new:
	count=0
	if i not in visited:
		for j in new:
			if i==j:
				count=count+1
			else:
				count=count
		print(i,count," ",end="")
		#print(i,end="")
		#print(count,end="")
		visited=visited+i





