'''
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''

N=int(input("enter Size = "))
list1=[]
count=0
for i in range(N):
	list1.append(input("Enter Element = "))
print(list1)
for i in range(len(list1)):
	for j in range(i+1,len(list1)):
		for k in list1[i]:
			if k in list1[j]:
				break
		else:
			print("{},{}".format(list1[i],list1[j]))		
			count+=1
print(count)
	
'''

n = int(input("enter array size :" ))
arr=[]
print("passwords :")
for i in range(n):
    arr.append((input()))
count=0
for i in range(len(arr)) :
    for j in range(i+1,len(arr)) :
        for k in arr[i]:
            if k in arr[j]:
                break
        else :
            print(F"{arr[i]},{arr[j]}")
            count+=1 

print(count)
'''