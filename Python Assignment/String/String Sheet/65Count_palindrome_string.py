#65. Count palindromic substrings in a string.

#S = "aaa"   o/p count =6 (a,a,a,aa,aa,aaa)

string=input("Enter string: ")

count=0
for i in range(len(string)):
    ch=string[i]
    b=ch[-1]
    if ch==b:
        count+=1
    for j in range(i+1,len(string)):
        ch=ch+string[j]
        a=ch[::-1]
        if ch==a:
            count+=1
print(count)