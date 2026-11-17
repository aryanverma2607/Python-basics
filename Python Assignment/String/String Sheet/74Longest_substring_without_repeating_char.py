#74. Find the longest substring without repeating characters.

string=input("Enter string: ")


l=[]
for i in range(len(string)):
    ch=string[i]
    l.append(ch)
    for j in range(i+1,len(string)):
        ch=ch+string[j]
        l.append(ch)
#print(l)

newlist=[]
for i in l:
    for j in i:
        if i.count(j)==1:
           continue
        else:
           break
    else:
         newlist.append(i)
#print(newlist)

highest=1
for i in newlist:
    if len(i)>=highest:
       highest=len(i)

for i in newlist:
    if len(i)==highest:
        print(i)
        break