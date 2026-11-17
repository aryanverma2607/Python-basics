def neon(n):
    sq=n**2
    sum=0
    while sq>0:
        r=sq%10
        sum=sum+r
        sq//=10
    if sum==n:
        return "Neon number"
    else:
        return "Not Neon number"