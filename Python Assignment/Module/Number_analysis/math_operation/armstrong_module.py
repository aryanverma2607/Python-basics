def armstrong(n):
    l=len(str(n))
    sum=0
    temp=n
    while n>0:
        r=n%10
        x=r**l
        sum+=x
        n//=10
    if temp==sum:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
