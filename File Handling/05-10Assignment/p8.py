'''8. Count Words Starting With a Particular Letter
A search engine wants to analyze words beginning with a particular character.
Write a Python program that:
1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.
Input File: article.txt
Python programming provides powerful features.
Programming helps developers build applications.

Sample Input:
Enter character: p
Expected Output:
Words starting with 'p': <display count>
'''
with open("article.txt","w") as f:
    f.write("""Python programming provides powerful features.
Programming helps developers build applications.""")
count=0
ch = input("Enter Character : ")
with open("article.txt","r") as f:
    text = f.read()
    for i in text.split():
            if i[0]==ch:
                count +=1
print(f"Words starting with '{ch}': {count}")
