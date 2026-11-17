#66. Count number of sentences in a paragraph.

paragraph=input("Enter Paragraph: ").lower()

count=0

for i in range(len(paragraph)):
    print(paragraph[i])
    if "a"<=paragraph[i]<="z" and paragraph[i+1]=='.' or paragraph[i+1]=="?" or paragraph[i+1]=="!":
        count+=1
print(count)