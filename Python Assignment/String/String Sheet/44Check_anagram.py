#44. Check if two strings are anagrams.

s1=input("Enter string:")
s2=input("Enter string:")

if len(s1)!=len(s2):
	print(len(s1)==len(s2))
else:
	a=sorted(s1)
	b=sorted(s2)
	print(a==b)

s=''
if len(s1)==len(s2):
    for i in s1:
      if i not in s:
        if s1.count(i)!=s2.count(i):
          print("Not anagram") 
          break
      s=s+i
    else:
        print("Anagram")