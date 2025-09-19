# # # def sample():
# # #     print("hello")


# # # x=sample


# # # li=[1,2,x,4]
# # # tu=(1,2,x,5)
# # # set1={1,4,6,x}
# # # dic={'x':x,'a':2}


# # # #a function is also an object
# # # #we can assign a function as a value to the variable
# # # #we can also use a function in a data structure(list,tuple,set,dictionaries)
# # # #we can also allow a function to pass as a argument into the other function
# # # #we can also allow a function  to take another function as a parameter
# # # #we can also allow a function to return another funcion.

# # # # higherorder function :

# # # #if a function takes another function as a arguement or returns another function then 
# # # # that function can be called as a higher order function.

# # # #callback function:
# # # # the function which we pass as a parameter into another function, that can be called
# # # #as a callback function.

# # # # def add (a,b):
# # # #     sum=a+b
# # # #     return sum
# # # # def sub(a,b):
# # # #     sub=a-b
# # #     # return sub 

# # # # def mul(a,b):
# # # #     mul=a*b
# # # #     return mul

# # # # def div(a,b):
# # # #     div=a/b
# # # #     return div
# # # # add=lambda a,b:a+b
# # # # sub=lambda a,b:a-b
# # # # mul=lambda a,b:a*b  
# # # # div=lambda a,b:a/b

# # # # def calc(fun,a,b):
# # # #     op=fun(a,b)
# # # #     return op 
# # # # op1=calc(lambda a,b:a+b,4,5)
# # # # op2=calc(lambda a,b:a-b,9,3)
# # # # op3=calc(lambda a,b:a*b,2,4)
# # # # op4=calc(lambda a,b:a/b,15,3)
# # # # print(op1)
# # # # print(op2)
# # # # print(op3)

# # # # def square(x):
# # # #     return x**2
# # # # def cube(x):
# # # #     return x**3
# # # def process(fun,li):
# # #     result=[]
# # #     for i in li:
# # #         sq=fun(i)
# # #         result.append(sq)
# # #     return result
# # # op1=process(lambda x:x**2,[1,2,3,4,5])
# # # op2=map(lambda x:x**3,[1,2,3,4,5])
# # # print(op1)
# # # print(list(op2))

# # # #here this process function is iterating every element in
# # # #the list and calling the function for every element of the list.

# # # #map is a builtin-higher order function which iterates everyelement in the (list/tuple/set) and 
# # # #performs a specific task using another function for each and every eleement.
# # # #map will returns always a new array.

# # # ip=['harish','sushma','Nandu','kiran','Naresh']
# # # # ['hi-harish','hi-sushma','hi-nandu','hi-kiran','hi-naresh']-->op
# # # op3=map(lambda x:'hi-'+x,ip)
# # # print(set(op3))

# # # #filter-->it is also a higher order function which can filter the elements in the list/tuple/set based on the 
# # # #condition and returns a new list/tuple/set

# # # ip1=[1,2,3,4,5,6,7,8,9,10]
# # # op4=map(lambda x:x%2==0,ip1)
# # # print(list(op4))

# # # li=[1,2,3,4,5]
# # # op=map(lambda x:x>3,li)
# # # print(list(op))

# # #reduce method

# # [1,5,8,2,9]
# # #finally it will give a single value as a o/p by reducing the given iterable object
# # #map-->iterates every element in list/tuple/set and performs task using a function and returns a new list/tuple/set
# # #filter-->iterates every element in list/tuple/set and performs task using a function and returns a new filtered list/tuple/set
# # #reduce-->iterates every element in list/tuple/set and performs task using a function and returns a single value.


# # #map--->len(ip)==len(op)
# # #filter-->len(ip)>=len(op)
# # #reduce-->returns single value

# # students_data=[{'name':'kiran'},{'name':'nandu'},{'name':'akhil'},{'name':'lakshmi'}]

# # def adding(d):
# #     d['city']='hyd'
# #     return d 
# # op=list(map(adding,students_data))

# # print(op)




# # # op_data=[{'name':'bmw','type':'vehicle'},
# # #          {'name':'thar','type':'vehicle'},
# # #          {'name':'benz','type':'vehicle'}]




# # #op=[{'name':'kiran','city':'hyd'},
# # # {'name':'nandu','city':'hyd'},
# # # {'name':'akhil','city':'hyd'},
# # # {'name':'lakshmi','city':'hyd'}]
# # # op=map(lambda x:x['city']='hyd',students_data)
# # # students_data[0]['city']='hyd'
# # # students_data[1]['city']='hyd'
# # # students_data[2]['city']='hyd'
# # # students_data[3]['city']='hyd'

# # # print(students_data)



# # # ip_data=[{'name':'bmw'},{'name':'thar'},{'name':'benz'}]

# # # def add(d):
# # #     d['type']='vehicle'
# # #     return d

# # # op=tuple(map(add,ip_data))
# # # print(op)


# # ip=[{'name':'samsung','type':'mobile'},
# #     {'name':'sony','type':'tv'},
# #     {'name':'lg','type':'tv'}]

# # #print dictionaries of only type-tv

# # op=list(filter(lambda x:x['type']=='tv',ip))
# # print(op)

from functools import reduce
# # li=[5,7,8,9,10,1,2,9,4]
# # reduce(func,iterable,startingvalue(optional))
# # op=reduce(lambda x,y:x+y,li,3)
# # op=reduce(lambda x,y:x if x>y else y,li)
# # print(op)

# # li=['i','love','my','india']
# # op=reduce(lambda x,y:x if len(x)>len(y) else y,li)
# #1-->x=i and y=love-->x>y--->love
# #2-->x=love and y=my-->x>y-->love
# #3-->x=love and y= india-->india
# #4-->x='india'

# # print(op)

# # op1=reduce(lambda x,y:x+' '+y,li)

# # print(op1)
# # 1-->x=5 and y=7
# # 2-->x=12 and y=8
# # 3--->x=20 and y=9
# # 4--->x=29 and y=10
# # 5-->x=39 
# #by default x value is first element in the list

# li=[1,4,7,9,0]
# op=14790
# op2=reduce(lambda x,y:x*10+y,li)
# print(op2)