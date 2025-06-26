# set_of_numbers={1,2,3,4,5,2,3,4}

# print(set_of_numbers) prints numbers in a set by ignoring duplicates

set1={"hi","js","css","python"}
# print(set1[2])

# set2=set1+{"1",4} #this can not be applicable for set because of unordered collection
# print(set2)
set1.add(4) #we can add extra element into the set using add method.

set1.remove("css") #it will removes the css from set
print(set1) #css was removed

#frozenset

fset=frozenset([3,5,7,9,2]) #it will create the frozenset of elements

print(fset)
# fset.add(9) #trying to add element into the frozenset.
#we cant add the elements into the frozenset
fset.remove(9) #remove cant use for frozenset

