'''
2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90
'''
l1=list(map(int,input("Traffic = ").split()))
pl1=[]
product=1
peakindex=-1
sum=0
for i in range(len(l1)):
	if i==0:
		if len(l1)==1 or l1[i]>=l1[i+1]:
			peakindex=i
			sum=sum+l1[peakindex]
			product=product*l1[peakindex]
			pl1.append(l1[peakindex])
	elif i==len(l1)-1:
		if len(l1)==0 or l1[i]>=l1[i-1]:
			peakindex=i
			sum=sum+l1[peakindex]
			product=product*l1[peakindex]
			pl1.append(l1[peakindex])
	else:
		if l1[i]>=l1[i-1] and l1[i]>=l1[i+1]:
			peakindex=i
			sum=sum+l1[peakindex]
			product=product*l1[peakindex]
			pl1.append(l1[peakindex])
print(pl1)
print("Sum = ",sum)
print("Product = ",product)
print("Max Peak = ",max(pl1))