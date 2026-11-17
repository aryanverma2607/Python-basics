s1=input("enter first string")
s2=input("enter second string")
string1=""
string2=""
for i in s1:
	if i==" ":
		continue
	else:
		string1=string1+i
for i in s2:
	if i==" ":
		continue
	else:
		string2=string2+i
if len(s1)!=len(s2):
    print("Not anagram")
else:
  
  x=1
  i=0
  while i<len(string1):
             ch=string1[i]
             c1=0
             c2=0
             j=0
             while j<len(string1):
                if string1[j]==ch:
                   c1=c1+1
                j=j+1
             j=0
             while j<len(string2):
                 if string2[j]==ch:
                    c2=c2+1
                 j=j+1
             if c1!=c2:
                 x=0
                 break
             
             i=i+1
  if x==1:
     print("anagram")
  else:
   print("not anagram")
