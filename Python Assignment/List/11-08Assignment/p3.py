'''
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45

'''
while True:
	print("""Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit""")
	choice=input("Emter your choice : ")
	if choice in "123":
		row=int(input("Enter Row size:"))
		column=int(input("Enter Column Size:"))
		list1=[]
		for i in range(row):
			r=[]
			for j in range(column):
				r.append(int(input("Enter Element of {} row :".format(i))))
			list1.append(r)
		for c in list1:
			print(*c)
		match choice:
			case '1':
				print("Highest total score")
				new=[]
			
				for a in range(row):
					sum1=sum(a)
					sum=0
					for b in range(column):
						sum=sum+list1[a][b]
					new.append(sum)
				print(new)
				print("Employee  {} has Highest Total Score = {}".format(i,max(new)))
					
			case '2':
				print("Lowest Average Score")
			case '3':
				print("Employee-wise Maximum Score")
	elif choice=='4':
		print("Exit")
		break
	else:
		print("Invalid choice")


