'''size=int(input("Enter size:"))
arr=[]
for i in range(size):
	arr.append(int(input("Enter number:")))
peakindex=-1
for i in range(size):
	if i==0:
		if size==1 or arr[i]>=arr[i+1]:
			peakindex=i
			break
	elif i==size-1:
		if size==size-1 or arr[i]>=arr[i-1]:
			peakindex=i
			break
	else:
		if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
			peakindex=i
			break
if peakindex!=-1:
	print("Peak index:",i)
	print("Peak value:",arr[peakindex])
'''
#sum of leaders in array 
#leader - an element is called a leader if it greater than all its rightmost element 
#rightmost element is always leader
#return sum of all leader
#if list is empty return -1
size=int(input("Enter size:"))
if size==0:
	print(-1)
else:
	arr=[]
	for i in range(size):
		arr.append(int(input("Enter number:")))
	leadersum=0
	for i in range(size):
		isleader=True	
		for j in range(i+1,size):
			if arr[i]<=arr[j]:
				isleader=False
				break
		if isleader:
			leadersum+=arr[i]
	print(leadersum)












