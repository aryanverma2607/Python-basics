#73. Find the longest palindromic substring.

s=input("Enter string:")

highest=1
l=[]
for i in range(len(s)):
    ch=s[i]
    b=ch[-1]
    if ch==b:
           if len(ch)>=highest:
               highest=len(ch)
               l.append(ch)
    for j in range(i+1,len(s)):
        ch=ch+s[j]
        a=ch[::-1]
        if ch==a:
            if len(ch)>=highest:
               highest=len(ch)
               l.append(ch)

for i in l:
    if len(i)==highest:
        print(i)