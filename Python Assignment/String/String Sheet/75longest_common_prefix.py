#75. Find the longest common prefix among strings.
# Strings = ["flower", "flow", "flight"] o/p = fl


string=input("Enter string:")

word=string.split()
ch=''
stop=False
for i in range(len(word[0])): #flower
    for j in range(1,len(word)):   #flght
        if i>=len(word[j]) or word[0][i] != word[j][i]:
            print("Longest Common Prefix:",ch)
            stop=True
            break
    if stop:
        break
    ch=ch + word[0][i]