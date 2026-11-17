'''6. Find the Longest Word
A document-processing application needs to identify the longest word in a text document.
Write a Python program that reads a file named "article.txt" and finds the longest word in the file.
Input File: article.txt
Python programming language is powerful.
Developers use Python for application development.
Expected Output:
Longest Word: programming
Length: 11
'''
with open("Article.txt","w") as f:
    f.write("""Python programming language is powerful
Developers use Python for application development""")
f.close()
word=[]
length = []
with open("Article.txt","r") as f:
    data = f.read()
    x = data.split()
    high=0
    l=""
    for i in x:
        if len(i)>high:
            l=i
            high=len(i)
    print(f"Longest Word:{l} and  length  is {high}")


        
