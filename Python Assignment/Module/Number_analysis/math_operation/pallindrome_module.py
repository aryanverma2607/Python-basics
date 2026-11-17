def pallindrome(n):
    rev=n[::-1]
    if rev==n:
        return "Pallindrome"
    else:
        return "Not Pallindrome"