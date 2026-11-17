'''
3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

'''
n=int(input("Enter size: "))
l1=[]
sq=0
for i in range(n):
	l1.append(int(input("Enter Element one by one : ")))
print(l1)
peak=[]
for i in range(n):
	if i==0:
		if n==1 or l1[i]>l1[i+1]:
			peakindex=i
			peak.append(l1[peakindex])
			sq=sq+l1[peakindex]**2
	elif i==len(l1)-1:
		if n==n-1 or l1[i]>=l1[i-1]:
			peakindex=i
			peak.append(l1[peakindex])
			sq=sq+l1[peakindex]**2
	else:
		if l1[i]>=l1[i-1] and l1[i]>=l1[i+1]:
			peakindex=i
			peak.append(l1[peakindex])
			sq=sq+l1[peakindex]**2
if peak==[]:
	print(-1)
else:
	print("Peak:",peak)
	print("Sum of square:",sq)
	average=sum(peak)//len(peak)
	print("Average = ",average)
	print("Difference = ",max(peak)-min(peak))





