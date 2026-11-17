'''7. Count Occurrence of a Particular Word
A company wants to analyze how frequently a particular keyword appears in a document.
Write a Python program that:
1. Reads a file named "article.txt".
2. Accepts a word from the user.
3. Counts how many times the given word occurs in the file.
Input File: article.txt
Python is simple.
Python is powerful.
Many developers use Python.
Python is popular.
Sample Input:
Enter word to search: Python
Expected Output:
Python occurs 4 times in the file.
'''
f = open("article.txt","w")
f.write("""Python is simple.
Python is powerful.
Many developers use Python .
Python is popular.""")
f.close()

count = 0
word = input("Enter a word to search:").lower()
with open("article.txt","r") as f1:
    text = f1.read().lower()
    for i in text.split():
        if word == i:
            count+=1
    print(f"{word} occurs {count} times in the file.")
