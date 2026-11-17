'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
'''
complaint=input("Enter complaint : ").lower()
b=complaint.split()
print(len(b))
''' 
'''
complaint=input("Enter complaint : ").lower()
i=0
count=0
while i<len(complaint):
	if complaint[i]!=" ":
		if complaint[i]>="a" or complaint[i]<="z":
			count=count+1
			while i<len(complaint):
				if complaint[i]>="a" and complaint[i]<="z":
					i=i+1
				else:
					break
				
		else:
			count=count
	else:
		count ==  count
	i=i+1
print(count)
'''

