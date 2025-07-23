# data=["hello","hi","welcome","ok"]
# op=[]
# for x in data:
#     # print(len(x))
#     op.append(len(x))
# print(op)
# [expression/operation iteration]
#to perform operation by iterating every element in 
# list/tuple/string/sets/dictionaries
# # in short and single line we can use comprehensions
# op=[len(x) for x in data] # operation and iteration
# print(op)

# list1=[2,4,6,8,11,5,7,9,21]
# op=[x*3 for x in list1]
# print(op)

#create a list of numbers from 5 to 10 using comprehensions
# op=[x for x in range(5,11)]
# print(op)

# #create a list of squares of numbers from 10 to 20 using comprehensions
# op1=[x**2 for x in range(10,21)]
# print(op1)


#convert every string to uppercase and create new list
# list1=["hi","HELLO","some","PYTHON","REACT","nodejs"]
# def casecnvrsion(x):   
#         if(x==x.upper()):
#             k=x.lower()
#             return k
#         else:
#             k=x.upper()
#             return k
# op2=[casecnvrsion(str) for str in list1]

# print(op2)

#reverse every string in list and create a new list from that using comprehensions
# list1=["python","java","html","react","css"]
# def rev(x):
#     revr=""
#     for i in range(len(x)-1,-1,-1):
#         revr+=x[i]
#     return revr

# op3=[rev(x) for x in list1]
# # op3=[x[::-1] for x in list1] #using string slicing
# print(op3)

# [expression iteration filteration]
# 1.iteration 
# 2.filteration 
# 3.expression

#1.iteration
#2.expression by filtering elements
#create a new list of strings by reversing them if they have
#length more than 4
# op4=[rev(x) for x in list1 if(len(x)>4)]
# print(op4)

# list1=[12,79,5,11,19,23,24,10]
#create list of numbers by subtracting 3 from numbers which are even

# op=[x-3 for x in list1 if(x%2==0)]
# op=[f"{x} is even" for x in list1]
# print(op)

def prime(num):
    isPrime=True
    for x in range(2,num):
        if(num%x==0):
            isPrime=False
            break
    if(isPrime):
        # print("num is prime")
        return True
    else:
        # print("num is not a prime")
        return False

lop=tuple(x for x in range(2,51) if(prime(x)))
print(lop)


#create list of first five armstrong numbers, perfect numbers,perfect squares,neon numbers and sunny numbers.



