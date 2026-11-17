#46. Check if a substring appears at both the start and end.

s1=input("Enter string:")
prefix=input("\nEnter Substring :")

print(s1.startswith(prefix) and s1.endswith(prefix))