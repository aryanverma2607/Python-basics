'''
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 170
'''
n=int(input("Enter Number of Houses ="))
sum=0
largest=1
i=1
while n>=i:
	units=int(input(f"House {i} Electricity units ="))
	if units<100:
		bill=units*5
		if units<50:
			bill1=bill-100
			print("House {} Bill ={}".format(i,bill1))
		else:
			bill1=units*5
			print("House {} Bill ={}".format(i,bill))
		if largest<bill1:
			largest=bill1
	elif units<200:
		bill2=5*100 + (units-100)*7
		print("House {} Bill ={}".format(i,bill2))
		if largest<bill2:
			largest=bill2
	else:
		bill3=5*100 + 7*100 + (units-200)*10
		print("House {} Bill ={}".format(i,bill3))
		if bill3>2000:
			bill3=bill3*0.1
		if largest<bill3:
			largest=bill3
	i=i+1
sum=sum+bill1+bill2+bill3
print("Total Collection =",sum)
print("Highest bill =",largest)