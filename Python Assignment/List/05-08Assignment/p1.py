'''
1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.
'''
l1=list(map(int,input("Elevation:").split()))
peakindex=-1
for i in range(len(l1)):
	if i==0:
		if len(l1)==0 or l1[i]>=l1[i+1]:
			peakindex=i
	elif i==len(l1)-1:
		if len(l1)==len(l1)-1 or l1[i]>=l1[i-1]:
			peakindex=i
	else:
		if l1[i]>=l1[i-1] and l1[i]>=l1[i+1]:
			peakindex=i
print(peakindex)


