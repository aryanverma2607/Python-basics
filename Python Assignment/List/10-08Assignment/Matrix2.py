print("""=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================
""")

while True:
	print("""1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit""")
	choice=int(input("enter Your Choice : "))
	match choice:
		case 1:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			l1=[]
			for i in range(r1):
				r=[]
				for j in range(c1):
					r.append(int(input(f"Enter {j} Element of {i} row:")))
				l1.append(r)
			for i in l1:
				print(*i)
			for k in range(len(l1)):
				count=0
				for j in l1[k]:
					num=j
					c1=0
					i=2
					while i<num//2:
						if num%i==0:
							c1=c1+1
						i+=1
					if c1==0:
						count+=1
				print(F"Row {k+1} prime count : {count}")
							
		case 2:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			l1=[]
			for i in range(r1):
				r=[]
				for j in range(c1):
					r.append(int(input(f"Enter {j} Element of {i} row:")))
				l1.append(r)
			for i in l1:
				print(*i)
			for k in range(len(l1)):
				count=0
				for j in l1[k]:
					num=j
					temp=num
					i=1
					while num>i:
						sum=0
						if num%i==0:
							sum=sum+i
						i+=1
					if sum>temp:
						count=count+1
				print(f"column {k+1} perfect number count : {count}")
						
					
		case 3:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			l1=[]
			for i in range(r1):
				r=[]
				for j in range(c1):
					r.append(int(input(f"Enter {j} Element of {i} row:")))
				l1.append(r)
			for i in l1:
				print(*i)
			for i in range(len(l1)):
				print("Row {} = {}".format(i,sum(l1[i])))
		case 4:
			print("Thank You for Using Matrix Analysis System")
			break