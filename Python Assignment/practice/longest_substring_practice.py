'''
Problem:1 Find the Longest Substring That Appears at Both Ends(4 marks)

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
1)  Input: ababcab Output: ab

2)  Input: level Output: l

3)  Input: abcabc Output: abc

4)  Input: abcdef Output: Not Found

5)  Input: aaaa Output: aaa*

Sample Test Cases

1)  Input: banana Output: Not Found

2)  Input: abcdabc Output: abc

3)  Input: xyzxyz Output: xyz

4)  Input: ababab Output: abab

5)  Input: mississippi Output: i

6)  Input: a Output: Not Found

7)  Input: aaaaaa Output: aaaaa

8)  Input: racecar Output: r

9)  Input: abababab Output: ababab

10) Input: abcab Output: ab
'''

string=input("Enter string: ")
substring1=[]
substring2=[]
ch=''
for i in range(len(string)):
    ch=ch+string[i]
    substring1.append(ch)
#print(substring1)
new=''
for j in range(-1,-len(string)-1,-1):
    new=string[j]+new
    #print(new)
    substring2.append(new)
#print(substring2)

l1=[]
for i in substring1:
    for j in substring2:
        if i==j:
           l1.append(i)
print(l1)
for i in range(-1,-len(l1)-1,-1):
   if len(l1[i])!=len(string):
        print(l1[i])
        break
else:
    print("Not found")
'''
s1 = input("enter the string=")
s2 = input("enter the string=")

if len(s1) == len(s2):
    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    print(count == 1)

elif abs(len(s1) - len(s2)) == 1:

    if len(s1) > len(s2):
        long = s1
        short = s2
    else:
        long = s2
        short = s1

    for i in range(len(long)):
        if long[:i] + long[i+1:] == short:
            print(True)
            break
    else:
        print(False)

else:
    print(False)
'''
