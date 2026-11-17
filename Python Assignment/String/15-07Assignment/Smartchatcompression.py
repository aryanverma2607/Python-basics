'''
QNO 7:
 Advanced Smart Chat Compression Expansion System

A messaging application stores repeated characters in compressed form to
reduce storage space. Before displaying messages to users, the system
should reconstruct the original message.

The application team has introduced additional rules.

Conditions: - Alphabet followed by number - Repeat character according
to the number - If alphabet is uppercase convert expanded characters
into lowercase - Ignore special symbols - Display expanded string -
Display total character count

Test Case 1 Input: Enter compressed message: a3

Output: Expanded Message: aaa

Total Characters: 3

Test Case 2 Input: Enter compressed message: A4b5

Output: Expanded Message: aaaabbbbb

Total Characters: 9

Test Case 3 Input: Enter compressed message: x2Y3

Output: Expanded Message: xxyyy

Total Characters: 5

Test Case 4 Input: Enter compressed message: m5@n2P4

Output: Expanded Message: mmmmmnnpppp

Total Characters: 11

Test Case 5 Input: Enter compressed message: R3S2t5

Output: Expanded Message: rrrssttttt

Total Characters: 10

'''

message=input("Enter Compressed message :").lower()
i=0
sum=0
a=""
while i<len(message):
	if message[i]>="a" and message[i]<="z":
		if message[i+1]>="0" and message[i+1]<="9":
			sum=sum+int(message[i+1])
			a=a+message[i]*int(message[i+1])
		else:
			a=a
	i=i+1
print(f"Expanded Message :{a}")
print("Total Characters: ",sum)	
























