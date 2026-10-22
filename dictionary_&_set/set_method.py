a={1,2,3,4,5,6,7}
print("Set is:",a)

# add element in set
a.add(8)
print("Add a element :",a)

# length of sets
print("Length of sets:",len(a))

# remove element in set
a.remove(7)
print("Remove element in set:",a)

# Remove an arbitrary(not fixed) element from the set
x=a.pop()
print("Element pop in set is:",x)
print("Set is:",a)

# Union
A={3,4,7,8}
B={1,2,3,5,6} 
C=A.union(B)
print("Union of set is:",C)

# intersection
D=A.intersection(B)
print("Intersection is:",D)