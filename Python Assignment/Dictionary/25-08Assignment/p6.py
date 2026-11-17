'''
6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

'''
l=[]
n=int(input("Enter number of city:"))
for i in range(n):
	cities=input("Enter city name:")
	l.append(cities)
d={}
for i in l:
	d[i]=d.get(i,0)+1
print(d)

c=max(d.values())
for k,v in d.items():
	if c==v:
		print(k)