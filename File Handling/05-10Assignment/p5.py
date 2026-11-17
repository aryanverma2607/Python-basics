'''5. Count Vowels and Consonants
A language-learning application wants to analyze the characters used in a paragraph.
Write a Python program that reads a file named "paragraph.txt" and counts:
1. Total number of vowels
2. Total number of consonants
Ignore numbers, spaces and special charact
ers.
Input File: paragraph.txt
Python Programming is Interesting.
Expected Output:
Total Vowels: <display count>
Total Consonants: <display count>
---
'''
vowel = 0
cons = 0
with open("paragraph.txt","r") as y:
    text = y.read().lower()
    for i in text:
        if i!="1234567890" or i!= " " or i!="!`~@#$%^&*()_+=-[]';:.,><":
            if i in "aeiou":
                vowel +=1
            elif i in "bcdfghjklmnpqrstvwxyz":
                cons +=1
print(f"""Total Vowels: {vowel}
Total Consonants: {cons}""")

