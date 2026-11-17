print("Compount Interest Calculator")
p,r,t=map(int,input("Enter principal,rate and time separated by space:").split())
Compound_interest=p*(1+(r/100))**t
print(p)
print(r)
print(t)
print("Total Amount=",round(Compound_interest))
print("Compound Interest=",round(Compound_interest-p))