'''
10.Lift Mode Operation – Advanced Smart Elevator System
A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  

The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1  
  Normal Up Mode activated.  

  Read current floor and destination floor.  

  Print all floors from current to destination in ascending order.

- Else if mode = 2  

  Down Mode activated.  

  Read current floor and destination floor.  

  Print all floors from current to destination in descending order.

- Else if mode = 3  

  Energy Saving Mode activated.  

  Read destination floor.  

  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else  

  Emergency Mode activated.  

  Print "Emergency Alarm" 4 times using loop.

Input:
3
6
Output:

0 2 4 6

Input:
1
2
7
Output:

2 3 4 5 6 7

Input:
2
8
3
Output:

8 7 6 5 4 3

Input:
5
Output:

Emergency Alarm

Emergency Alarm

Emergency Alarm

Emergency Alarm
'''
'''
Write a program:
- Else  

  Emergency Mode activated.  

  Print "Emergency Alarm" 4 times using loop.

'''
while True:
	a=int(input("Enter Mode = "))
	if a==1:
		print("Normal Mode Activated")
		x=int(input("Enter Current Floor = "))
		y=int(input("Enter Destination Floor = "))
		for i in range(x,y+1):
			print(i,end=" ")
		break
	elif a==2:
		print("Down Mode Activated")
		x=int(input("Enter Current Floor = "))
		y=int(input("Enter Destination Floor = "))
		for i in range(x,y-1,-1):
			print(i,end=" ")
		break
	elif a==3:
		print("Energy Saving Mode Activated")
		y=int(input("Enter Destination Floor = "))
		for i in range(0,y+1,2):
			print(i,end=" ")
		break
	else:
		print("Emergency Mode Activated")
		n=4
		i=0
		while i<n:
			print("Emergency Alarm")
			i=i+1
		break






























