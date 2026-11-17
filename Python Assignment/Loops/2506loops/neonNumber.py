'''9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number
'''
n=int(input("Number = "))

temp=n
sq=n**2
a=len(str(sq))
sum=0
while sq>0:
	rem=sq%10
	sum=rem+sum
	sq=sq//10
print(sum)
if sum==temp:
	print("Glowing Success! You've found the Neon Number!")
else:
	print("Try again! Not quite glowing yet.")



'''
for i in range(1,a+1):
	rem=sq%10
	sum=sum+rem
	sq=sq//10
	a=a+1
print(sum)
if sum==temp:
	print("Glowing Success! You've found the Neon Number!")
else:
	print("Try again! Not quite glowing yet.")

'''
	