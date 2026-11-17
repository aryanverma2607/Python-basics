def perfect(n):
    total=0
    temp=n
    for i in range(1,n):
        if n%i==0:
            total+=i
    if total==temp:
        return "Perfect number"
    else:
        return "Not perfect number"