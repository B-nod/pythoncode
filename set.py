a = {1,2,3,4,5}
a.add(6)
a.add("Nepal") #adds the given item to the set
print(a)
b = {6,7,8,9,10} 
a.update(b) #update the item of b in a
print(a)
a.remove(5) # removes given item from  the set
print(a)
b = a.copy() # makes copy of given set
print(b)
b.clear() #clear all the items from the set
print(b)
# difference
A = {'a', 'b', 'c', 'd', 'e'}
B = {'f', 'b', 'c', 'd', 'g'}
print(A.difference(B)) #gives only the value of A which is not present in B
print(A.intersection(B)) #gives the common values of A and B
print(A.isdisjoint(B)) #gives true if A and B contain differnce values and false if both contain some similar values
print(A.issubset(B)) #gives true if B contain all values present in A 

removed_element = a.pop() #removes random item from the list
print(removed_element)
y = {'a','b','c','d'}
removed_element_y = y.pop()
print(removed_element_y)
print(A.symmetric_difference(B)) #Returns all the items present in given sets, except the items in their intersection
print(A.union(B))
