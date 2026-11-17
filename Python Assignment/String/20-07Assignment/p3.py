'''
3. Secure Banking Transaction Analyzer
A banking server generates encrypted transaction IDs using letters and digits.
The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:
text
No unique digit found

### Input:
text
A122334455667789
### Output:
text
8
'''
string=input("Input : ")
c1=0
for i in string:
	if "0"<=i<="9":
		for j in string:
			if "0"<=j<="9":
				if i==j:
					continue
				else:
					break
			else:
				continue
	else:
		continue
	break
print(i)

		
