#60. Append two strings but remove duplicate adjacent characters.

#S1="miss", S2="issippi"   "misisipi"

s1=input("Enter String:")
s2=input("Enter String:")

n=''
s=s1+s2
for i in range(len(s)):
	if i==0 or s[i]!=s[i-1]:
		n=n+s[i]
print(n)

