'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''

message=input("Enter message: ").split()
i=0
result=""
print("Encrypted message:",end="")
while i<len(message):
	a=message[i]
	b=a[::-1]
	result=result+b
	i=i+1
print(len(result))
print(result)



	


