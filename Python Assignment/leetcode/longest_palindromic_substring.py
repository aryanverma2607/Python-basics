'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"'''
s="babad"
high=0
l=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        ch = s[i:j+1]
        if ch == ch[::-1]:
            l.append(ch)
for i in l:
    if len(i)>high:
        high = len(i)
for i in l:
    if len(i) == high:
        print(i)
        break


# time complexity O(1) chahiye isme