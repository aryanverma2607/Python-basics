'''4. Count Lines, Words and Characters in a File
A content management company wants to analyze the size of a text document.
Write a Python program that reads a file named "article.txt" and displays:
1. Total number of lines
2. Total number of words
3. Total number of characters
Input File: article.txt
Python is easy.
Python is powerful.
Python is widely used in industry.
Expected Output:
Total Lines: 3
Total Words: 14
Total Characters: <calculate based on file content>
'''
with open("article.txt","r") as f:
    data = f.read()
    print(f"""Total Lines: {len(data.splitlines())}
Total Words: {len(data.split())}
Total Characters: {len(data)}""")
