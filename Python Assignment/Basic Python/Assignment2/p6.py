#Exercise 6
print("Smart Coin Machine")
amount=int(input("Enter amount in multiple of 5:"))
division10=amount//10
multiple5=amount-division10*10
change5=multiple5//5
print("output=$10 x ",division10,", 5 x ",change5)
