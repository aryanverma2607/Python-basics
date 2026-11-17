'''
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789
'''
ticket=input("Enter number = ").upper()
count=0
number=0
count1=0
if len(ticket)!=12:
	print("Invalid PNR")
else:
	if ticket[0]=="P" or ticket[1]=="N" or ticket[2]=="R":
		count=1
	i=0
	while i<len(ticket):
		ch=ticket[i]
		if ch>="0" and ch<="9":
			number=number+1	
		else:
			count1=count1+1
		i=i+1
	if count==1 and number==9:
		print("Valid PNR number")
	else:	
		print("Invalid PNR")






