'''
name=["suleman","sham","ram"]
marks=[34,54,43]
print(name)
print(marks)
student=input("Enter student name:")
if student in name:
	index=name.index(student)
	newmarks=int(input("Enter New marks:"))
	marks[index]=newmarks
else:
	print("St. not found")
print(marks)
'''
'''
a=[1,2,2,3]
print(a.pop())
print(a)
print(a.pop(0))
print(a)
'''
'''
a=[1,2,3,4]
print(a)
print(a[:])   #it will create copy of list
'''
items=["pen","book","bag"]
print(items)
name=input("Enter item to remove")
if name in items:
	items.remove(name)
else:
	print("item not found")
print(items)











