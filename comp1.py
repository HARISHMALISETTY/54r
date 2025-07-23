#tuple comprehension


# str="something"

# op=tuple(x for x in str)
# print(op)


#generate tuple of pair of num and its square 

# ((2,4),(3,9),(4,16),(5,25))

# op1=tuple((x,x**2) for x in range(1,6))
# print(op1)

# str1="tuple comprehensions"

# op1=tuple(x for x in str1 if x in "aeiouAEIOU")
# print(op1)

# op1={x for x in str1 if x in "aeiouAEIOU"}
# print(op1)


# dic={"a1":"one","a2":"two"}
# print(dic)

# str1="something"
# op1={'x':x for x in str1}
# print(op1)

# list1=["js","html","css","python","react"]

# #op={0:"js",1:"html",2:"css",3:"python",4:"react"}

# op={x:list1[x] for x in range(len(list1))}

# print(op)
dict1={"stu1":"kiran","stu2":"nandini","stu3":"ajay","stud4":"vishnu"}

# op={"stu1":"kiran-10000coders","stu2":"nandini-10000coders",
#     "stu3":"ajay-10000coders","stud4":"vishnu-10000coders"}

op={x:dict1[x]+"-10000coders" for x in dict1}
print(op)