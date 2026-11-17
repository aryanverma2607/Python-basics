n=int(input("enter the number"))
sum=0
product=1
while n>0:
     d=n%10
     if d%2==0:
          sum=sum+d
     else:
          product=product*d
     n=n//10



print("sum is",sum)
print("product is",product)


 


