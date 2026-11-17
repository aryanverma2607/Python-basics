'''
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''
sentence=set()
missing=set()
while True:
	print("""Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit""")
	choice=(input("Enter choice : "))
	match choice:
		case '1':
			s=input("Enter Sentence = ").lower()
			sentence=set(s)
			print(sentence)
		case '2':
			if sentence!=set():
				character=[]
				for i in range(97,123):
					ch=chr(i)
					if ch not in sentence:
						character.append(ch)
				missing=set(character)
				print(missing)	
		case '3':
			if missing!=set():
				print("Missing Alphabets = ",len(missing))
		case '4':
			print("Exit")
			break
		case __:
			print("Invalid Choice")