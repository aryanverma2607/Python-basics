print("Change Return System")
amount=int(input("Enter amount:"))
change100=amount//100
change50=(amount-change100*100)//50
change10=(amount-change50*50-change100*100)//10
print("Amount = ",amount)
print("₹100 x ",change100)
print("₹50 x ",change50)
print("₹10 x ",change10)