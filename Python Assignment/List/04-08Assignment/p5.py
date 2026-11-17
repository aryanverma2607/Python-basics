'''
5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---
 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5

'''
marks=list(map(int,input("Enter Marks:").split()))
a=[]
b=[]
c=[]
fail=[]
print(marks)
for i in marks:
	if i>=90:
		a.append(i)
	elif 75<=i<90:
		b.append(i)
	elif 50<=i<75:
		c.append(i)
	else:
		fail.append(i)
print("""===== STUDENT GRADE REPORT =====

A Grade Students   : {}
B Grade Students   : {}
C Grade Students   : {}
Fail Students      : {}

--------------------------------
A Count   : {}
B Count   : {}
C Count   : {}
Fail Count: {}
--------------------------------

Total Students: {}""".format(a,b,c,fail,len(a),len(b),len(c),len(fail),len(a)+len(b)+len(c)+len(fail)))