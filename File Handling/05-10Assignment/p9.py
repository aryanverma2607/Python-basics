'''9. Find the Most Frequently Used Word
A content-analysis application wants to identify the most frequently used word in an article.
Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.
Input File: article.txt
Python is easy.
Python is powerful.
Python is popular.
Java is also popular.
Expected Output:
Most Frequently Used Word: Python
Frequency: 3
'''
with open("article.txt","w") as f:
    f.write("""Python is easy.
Python is powerful.
Python is popular.
Java is also popular.""")

word=[]
frequent = []
with open("article.txt","r") as f1:
    text = f1.read().split()
    for i in text:
        if i not in word:
            c = text.count(i)
            frequent.append(c)
            word.append(i)
    high = max(frequent)
    index = frequent.index(high)
    print(f"""Most Frequently Used Word: {word[index]}
Frequency: {high}""")