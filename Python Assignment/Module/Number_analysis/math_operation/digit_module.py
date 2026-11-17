def digit(n):
    count=0
    while n>0:
        r=n%10
        if 0<=r	<=9:
            count+=1
        n//=10
    return count