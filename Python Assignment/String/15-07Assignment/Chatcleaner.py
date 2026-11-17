'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy

'''
message=input(" Enter message : ")
i=0
new=""
while i<len(message):
	ch = message[i]
	if (message[i]==" " and message[i-1]==" "):
		pass
	else:
		new=new+ch
	i=i+1
new=new.lstrip()
print(len(new))
print(new)		
	