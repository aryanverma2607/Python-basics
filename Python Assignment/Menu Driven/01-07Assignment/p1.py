'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit
'''
while True:
	print("1. Check Prime Number")
	print("2. Check Palindrome Number")
	print("3. Reverse a Number")
	print("4. Count Digits")
	print("5. Exit")
	n=int(input("Enter Option = "))
	match n:
		case 1:
			n=int(input("Enter number = "))
			i=2
			count=0
			while i<n//2:
				if n%i==0:
					count=count+1
				i=i+1
			else:
				if count>0:
					print(f"{n} is not a Prime number")
				else:
					print(f"{n} is prime number")
		case 2:
			n=int(input("Enter number = "))
			m=n
			rev=0
			for i in range(len(str(n))):
				r1=n%10
				rev=rev*10+r1
				n=n//10
			else:
				if rev==m:
					print(f"{m} is not a Pallindrome number")
				else:
					print(f"{m} is not Pallindrome number")
		case 3:
			n=int(input("Enter number = "))
			rev=0
			for i in range(len(str(n))):
				r1=n%10
				rev=rev*10+r1
				n=n//10
			print("Reverse number = ",rev)
		case 4:
			n=int(input("Enter number = "))
			i=2
			count=0
			while n>0:
				r=n%10
				count=count+1
				n=n//10
			print("Count Digit = ",count)
		case 5:
			print("EXIT")
			break
	a=input("Do you want to Proceed further(yes/no) = ").lower()	
	match a:
		case "yes":
			continue
		case "no":
			break
		case __:
			print("Provide Correct input")