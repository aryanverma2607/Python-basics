#10. Trim leading,trailing,or extra spaces from a string.

s=input("Enter String : ")
s1=s.strip()
s2=''
for i in range(len(s1)):
	if s1[i]==" " and s1[i+1]==" ":
		continue
	else:
		s2=s2+s1[i]
print(s2) 
