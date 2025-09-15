def sample():
    print("hello")


x=sample


li=[1,2,x,4]
tu=(1,2,x,5)
set1={1,4,6,x}
dic={'x':x,'a':2}


#a function is also an object
#we can assign a function as a value to the variable
#we can also use a function in a data structure(list,tuple,set,dictionaries)
#we can also allow a function to pass as a argument into the other function
#we can also allow a function  to take another function as a parameter
#we can also allow a function to return another funcion.

# higherorder function :

#if a function takes another function as a arguement or returns another function then 
# that function can be called as a higher order function.

#callback function:
# the function which we pass as a parameter into another function, that can be called
#as a callback function.

# def add (a,b):
#     sum=a+b
#     return sum
# def sub(a,b):
#     sub=a-b
    # return sub 

# def mul(a,b):
#     mul=a*b
#     return mul

# def div(a,b):
#     div=a/b
#     return div
# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# mul=lambda a,b:a*b  
# div=lambda a,b:a/b

# def calc(fun,a,b):
#     op=fun(a,b)
#     return op 
# op1=calc(lambda a,b:a+b,4,5)
# op2=calc(lambda a,b:a-b,9,3)
# op3=calc(lambda a,b:a*b,2,4)
# op4=calc(lambda a,b:a/b,15,3)
# print(op1)
# print(op2)
# print(op3)

# def square(x):
#     return x**2
# def cube(x):
#     return x**3
def process(fun,li):
    result=[]
    for i in li:
        sq=fun(i)
        result.append(sq)
    return result
op1=process(lambda x:x**2,[1,2,3,4,5])
op2=map(lambda x:x**3,[1,2,3,4,5])
print(op1)
print(list(op2))

#here this process function is iterating every element in
#the list and calling the function for every element of the list.

#map is a builtin-higher order function which iterates everyelement in the (list/tuple/set) and 
#performs a specific task using another function for each and every eleement.
#map will returns always a new array.

ip=['harish','sushma','Nandu','kiran','Naresh']
# ['hi-harish','hi-sushma','hi-nandu','hi-kiran','hi-naresh']-->op
op3=map(lambda x:'hi-'+x,ip)
print(set(op3))

#filter-->it is also a higher order function which can filter the elements in the list/tuple/set based on the 
#condition and returns a new list/tuple/set

ip1=[1,2,3,4,5,6,7,8,9,10]
op4=map(lambda x:x%2==0,ip1)
print(list(op4))




