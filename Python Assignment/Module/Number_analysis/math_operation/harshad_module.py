def harshad(n):
    sum=0
    temp=n
    while n>0:
        r=n%10
        sum=sum+r
        n//=10
    if temp%sum==0:
        return "Harshad Number"
    else:
        return "Not Harshad Number"