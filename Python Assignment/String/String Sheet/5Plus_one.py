#5. Plus one

n=int(input("Enter size of list: "))
digits=[]

for i in range(n):
    a=int(input("Enter elment: "))
    digits.append(a)
s=0
for i in digits:
   s=s*10+i
   b=s+1
   res=[]
   for i in str(b):
       res.append(int(i))
       print(res)