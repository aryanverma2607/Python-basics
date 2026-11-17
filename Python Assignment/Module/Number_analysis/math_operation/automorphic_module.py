def automorphic(n):
    l=len(str(n))
    sq=n*n
    if sq%10**l==n:
        return "Automorphic number"
    else:
        return "Non Automorphic number"