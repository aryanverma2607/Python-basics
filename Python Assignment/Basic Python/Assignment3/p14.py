print("Simple Profit or Loss Calculator")
cp=int(input("Enter cost price:"))
sp=int(input("Enter selling price:"))
profit=sp - cp
percentage=profit//10
print("+ve indicates Profit and negative indicates Loss")
print("Profit/Loss={}".format(profit))
print("Profit/Loss % ={}".format(percentage))
