#72. Print all substrings of length n.

string=input("Enter string: ")
n=int(input("Enter length pf substring:"))

count=0
for i in range(len(string)):
    ch=string[i]
    if len(ch)==n:
        print(ch,end=" ")
    for j in range(i+1,len(string)):
        ch=ch+string[j]
        if len(ch)==n:
            print(ch,end=" ")