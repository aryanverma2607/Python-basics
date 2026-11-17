'''
QNO 2: Find the Longest Substring That Appears at Both Ends(3.5 marks)

Problem Statement Given a string S, find the longest substring that
appears both as a prefix (beginning) and as a suffix (ending) of the
string.

The prefix and suffix must not be equal to the entire string itself. If
multiple such substrings exist, return the longest one. If no such
substring exists, print “Not Found”.

Note: The prefix and suffix may overlap.

Input Format - A single line containing the string S.

Output Format - Print the longest substring that appears as both a
prefix and a suffix. - If no such substring exists, print: Not Found

Constraints 1 ≤ |S| ≤ 100000 S consists of lowercase English letters
only.

'''


string=input("Enter string: ")
s1=[]
s2=[]
ch=''
for i in range(len(string)):
     ch=ch+string[i]
     s1.append(ch)
#print(s1)
new=''
for i in range(-1,-len(string)-1,-1):
     new=string[i]+new
     s2.append(new)
#print(s2)
newlist=[]
for i in range(len(s1)):
     for j in range(len(s2)):
        if s1[i]==s2[j]:
            newlist.append(s1[i])
#print(newlist)


for i in range(-1,-len(newlist)-1,-1):
      if len(newlist[i])!=len(string):
          print(newlist[i])
          break
else:
    print("Not found")



'''
sub=""
for i in range(len(string)):
     a=string[:i]
     b=string[-(i+1):]
     if a==b:
        sub=a
        print(sub)
'''