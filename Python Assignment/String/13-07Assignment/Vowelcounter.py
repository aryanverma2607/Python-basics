'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''


'''
a=input("Enter String = ").lower()
vowel=0
i=0
while i<len(a):
	ch=a[i]
	if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
		vowel=vowel+1
	i=i+1
print(f"Total Vowels {vowel}")
'''
a=input("Enter String = ").lower()
b=a.count("a")
c=a.count("i")
d=a.count("e")
e=a.count("o")
f=a.count("u")
s=b+c+d+e+f
print(f"Total vowels {s}")