#cyclically rotate Array by one position
'''l1=list(map(int,input("Enter Element one by one:").split()))
print(l1)
a=l1.pop(len(l1)-1)
l1.insert(0,a)
print(l1)
'''
'''
n=int(input("Enter size:"))
arr=[]
i=0
while i<n:
	arr.append(int(input("Enter elemant : ")))
	i+=1
last=arr[n-1]
i=n-1
while i>0:
	arr[i]=arr[i-1]
	i-=1
arr[0]=last
print(arr)
'''
'''
#find the number of pairs of element in the array whose sum is equal to K.
l1=list(map(int,input("Enter elements: ").split()))  #1 5 7 1 2 k=6
k=int(input("Enter Sum: "))
count=0
for i in range(len(l1)):
	for j in range(i+1,len(l1)):
		if l1[i]+l1[j]==k:
			count=count+1
print("Number of pairs:",count)
'''
'''
# list comprehension:
# [expression for item in iterable]
# conditional statement in LC:
#[expression for item in iterable if condition]
a=[1,2,3,4,5]
#b=[i for i in a if i%2==0]
b=[i*10 if i%2==0 else i*20 for i in a]
print(b)
'''
'''
#nested list
a=[[1,2,9],[3,4,7],[5,6,8]]
print(a)
#print(a[2][2]) error
#print(a[2])
#print(a[2][1])
# element in 2 d array row-wise
#for i in a:
#	print(i)
print("to iterate each element of 2 d array")
for i in a:
	for j in  i:
		print(j,end=" ")
	print()
print("Traversing using index")
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j],end=" ")
	print()
'''
'''
print("Rotating list ")
l1=list(map(int,input("Enter element separated by space : ").split()))
# 1,2,3,4,5
last=l1[len(l1)-1]
for i in range(len(l1)-1,0,-1):
	l1[i]=l1[i-1]
l1[0]=last
print(l1)
'''
'''
print("Find pair of element equal to given sum K")
arr=list(map(int,input("Enter element separated by space : ").split()))
k=int(input("Enter sum : "))
count=0
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if i+j==k:
			print(i,j)
			count=count+1
print(count)
'''





















