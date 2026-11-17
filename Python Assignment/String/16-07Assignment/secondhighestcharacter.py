'''
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found


'''


msg = input("Input: ")
msg = "".join(msg)
largest=0
second=0
lc=""
sc="" 
i = len(msg)-1
while i>=0:
        count=0
        j = len(msg)-1
        while j>=0:
                if msg[i] == msg[j]:
                     count+=1
                j-=1
        if count>largest :
                second = largest
                sc = lc
                lc = msg[i]
                largest = count

        i-=1
print(lc," occurs ",largest," times → highest")        
if second == 0:
      print("Second highest repeating character not found")
else:
      print(sc," occurs ",second," times → second highest")



