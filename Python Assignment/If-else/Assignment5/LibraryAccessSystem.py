'''9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books
'''
membership=input("Membership is Active(Yes/No) ").lower()
book_issued=int(input("Enter number of book issued:"))
if membership=="yes":
	print("Entry Allowed")
	if book_issued<3:
		print("Can issue more Books")
	