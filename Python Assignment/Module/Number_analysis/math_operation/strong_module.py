def strong(n):
    total=0
    temp=n
    while n>0:
        r=n%10
        fact=1
        for i in range(1,r+1):
            fact=fact*i
        total=total+fact
        n//=10
    if temp==total:
        return "Strong number"
    else:
        return "Not Strong number"