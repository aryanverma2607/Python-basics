#71. Print all substrings of a string.

string=input("Enter string: ")


for i in range(len(string)):
    ch=string[i]
    print(ch,end=" ")
    for j in range(i+1,len(string)):
        ch=ch+string[j]
        print(ch,end=" ")