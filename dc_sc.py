import copy


# # # x={'name':'harish','city':"hyd"}
# # x={
# #     'user':{'name':'harish','gender':'male'},
# #    'city':'hyd'
# #    }

# # x1=copy.copy(x)
# # x2=copy.copy(x)


# # print(x1)
# # print(x2)

# # x1['user']['name']='naresh'

# # print(x1)
# # print(x2)
# # print(x)

# x={'user':{'name':'harish','gender':'male'},'city':'hyd'}
# x1=copy.copy(x)
# x2=copy.copy(x)

# x1['user']['name']='naresh'

# print(x,'main')
# print(x1,'copied1')
# print(x2,'copied2')


# match={'score':{'runs':125,'wickets':2},'overs':5}
# comm_a=copy.copy(match)
# comm_b=copy.copy(match)
# comm_a['score']['runs']+=6

# print(match)
# print(comm_a)
# # print(comm_b)


# pubg={'score':{'kills':0,'health':100}}

# ganesh=copy.deepcopy(pubg)
# akash=copy.deepcopy(pubg)
# srikanth=copy.deepcopy(pubg)
# akash['score']['kills']+=4

# print(pubg)
# print(ganesh)
# print(akash)
# print(srikanth)

#shallow copy-->will copies the objects with respect to their reference.
#if changes applies in copied, then it will reflects to all the objects
#  of same referrence

#deep copy--will copies the values inside the objects irrespective 
# to the reference and
#create new reference for all copies created
#if changes applied in copied, then it won't reflects to others
#  because of different referrence.

# def open_box(n):
#     if n>1:
#         print(f"box{n} opened")
#         open_box(n-1)
#     else:
#         print(f"found the gift in box {n}")
# open_box(5)


#find the factorial of given num using recurive function.



# 5--->5*4*3*2*1

# def factorial(n):
#     fact=1
#     if n==0 or n==1:
#         return fact
#     else:
#         fact=n*factorial(n-1)
#         return fact
# print(factorial(5))

# factorial(5)
# factorial(4)
# factorial(3)
# factorial(2)
# factorial(1)



x=[1,2,3,[4,5,6,[1,2,3,[1,2,3]]],[5,6,7]]
sum=0
for i in x:
    if isinstance(i,list):
        for j in i:
            sum+=j
    else:
        sum+=i
print(sum)

# x=[1,2,3]
# op=isinstance(x,list)
# print(op)