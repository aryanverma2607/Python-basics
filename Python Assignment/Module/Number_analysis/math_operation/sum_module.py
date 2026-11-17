def sum(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n//=10
    return sum