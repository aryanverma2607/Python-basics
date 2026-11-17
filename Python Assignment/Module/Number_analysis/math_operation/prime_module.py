import math
def prime(n):
    c=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            c+=1
    if c==0:
        return "Prime number"
    else:
        return "Non Prime number"
