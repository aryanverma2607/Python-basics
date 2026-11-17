'''
#filter(function,iterable)
#WAP to filter names of students whose length is greater then 5

names=["Aryan","niteen","diggy","madam"]

print(list(filter(lambda x:len(x)>5,names)))

#write a program to filter all the palindrome number

print(list(filter(lambda x:x==x[::-1],names)))
'''
'''
#reduce()
numbers=[1,2,3,4,5,6]
from functools import reduce
print(reduce(lambda x,y:x*y,numbers))    #o/p = 720

#WAP to find maximum element in a list using reduce
numbers=[1,2,3,4,5,6]

result=reduce(lambda x,y:x if x>y else y,numbers)
print(result)


#WAP to concatenate strings in a list using reduce
nums=["abc","def","wert","aryan"]

print(reduce(lambda x,y:x+" "+y,nums))
'''
'''
#lambda in sorting
products=[
   {"name":"laptop","price":8000},
   {"name":"refrigerator","price":6000},
   {"name":"tab","price":2000},

]


result=sorted(products,key=lambda x:x["price"])
print(result)
'''
#WAP to filter names of students whose length is greater then 5
def lenght(x):
    l=[]
    if len(x)>5:
       l.append(x)
    return l
numbers=['12','13','121','22','33','151','234432','56','767','890']
print(list(filter(lenght,numbers)))
names=["aryan","digvijay","niteen","krishna","aryanapatider","palak","muskan"]
result=list(filter(lambda x:len(x)>5,names))
print(result)

#write a program to filter all the palindrome number
numbers=['12','13','121','22','33','151','234432','56','767','890']
print(list(filter(lambda x:x==x[::-1],numbers)))         
#          filter(function_____name_,iterable)

def pallindrome(x):       #normal function
    l=[]
    if x==x[::-1]:
       l.append(x)
    return l

print(list(filter(pallindrome,numbers)))

#filter function generates list of data while condition is true


















