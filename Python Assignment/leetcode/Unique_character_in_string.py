'''First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1'''
s="leetcode"
# d = {}
# for i in s:
#     d[i] = d.get(i,0) + 1
# for j in range(len(s)):
#     if d[s[j]] == 1:
#         print(j)
# else:
#     print("-1")

s = "abcd"
t = "abcd"
S = set(s.split())
T = set(t.split())
print(S,T)
print(S-T)