#union
s={"Aryan","Krishna","Sahil"}
s1={"Aryan","Niteen","Digvijay"}
#print(s)
#print(s|s1)
print("Union = :",s.union(s1))

#intersection
print(s&s1)
#Difference
print(s-s1)
print("intersection",s.difference(s1))

#symmetric difference
s={10,20,3,2,40}
s1={2,3,4,1}
print(s^s1)
#print("symmetric difference",s.symmetric_difference(s1))

#subset
s={10,20,3,2,40}
s1={2,3,4,1}
print(s<=s1)   # All element of s is present in s1
#print("Subset",s.issubset(s1))

#superset
b={1,2,3,4,5}
a={1,2}
#print(b>=a)
print("Superset",b.issuperset(a))

#disjoint set
a={1,2,3,4,5}
b={1,2}
print("Disjoint set : ",a.isdisjoint(b))

#inplace union
s={10,20,3,2,40}
s1={2,3,4,1}
s1.update(s)
print(s1)
s1|=s  #in place union
print("Inplace union",s1)

#intersection_update
s={10,20,30,20,40,5}
s1={10,20,30,1,2,3,5}
s.intersection_update(s1)
s&=s1
print("Intersection_ update",s)

#difference_update
s={10,20,30,20,40,5}
s1={10,20,30,1,2,3,5}
s.difference_update(s1)
s-=s1
print("difference_update",s)


#Symmetric_difference_update
s={10,20,30,20,40,5}
s1={10,20,30,1,2,3,5}

s^=s1
print("Symmetric_difference_update",s)