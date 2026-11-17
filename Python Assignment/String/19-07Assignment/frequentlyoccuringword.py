'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
'''
text=input("Input : ").split()
list1=[]
for i in text:
	count=0
	if i not in list1:
		for j in range(len(text)):
			if i==text[j]:
				count=count+1
			else:
				count=count
		list1=list1.append(i)
		print(i,count)
