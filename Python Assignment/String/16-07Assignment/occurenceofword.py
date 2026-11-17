'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:

```
iphone is good and iphone battery is strong
```

Word:

```
iphone
```

Output:

```
2
```

'''
string=input("Input Sentence: ").split()
ch=input("Enter Word to find : ")
i=0
for s in string:
	if s==ch:
		i+=1
	else:
		i=i
print("Output : ",i)