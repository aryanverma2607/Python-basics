#41. Check if a string contains a substring (without using contains()).

#S1 = "Hello", Sub="ell"

string=input("Enter string: ")
s=input("Enter Substring: ")

print(s in string)
print(string.__contains__(s))
