#3754. Concatenate Non-Zero Digits and Multiply by Sum I
n=10203004
b=str(n)
sum=0
s="0"
for i in b:
    if i!="0":
        s=s+i
        sum=sum+int(i)
    print(s,sum)
    c=int(s)*sum
print(c)