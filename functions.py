# # def sample():
# #     print("hello")
# #     return "hii"
# # x=sample()
# # print(x)


# def sample():
#     print("hii")
#     return 
# print(sample())

# #return -->is used to return something from the function definition
# #by default function will returns None if we dont return any value.
# always count of args and params should be equal
# def demo(x,y,z):
#     print(x+y+z)

# demo(1,2,3)



# 250+(0.18*250)
def billing(price,gst=0.18):
    total_price=(price+gst*price)
    return total_price

# print(billing(125))
# print(billing(175))
# print(billing(250))
# print(billing(250,0.28))

# def cart(*x):
#     print(x)
# cart("chains","books","pens",
#      "clothes","makeup-kits",
#      "deodrants","shoes","watches")

# #whenevr u dont know the exact count of args, 
# # then we can go with arbitrary args (*args)

# def bahubhali(hero,villain,heroine):
#     print(f"hero:{hero}, heroine:{heroine}, villain:{villain}")


# bahubhali(heroine="anushka",hero="prabhas",villain="raana")

def bahubhali(**cast):
    print(cast)

# bahubhali(heroine="anushka",
#           hero="prabhas",
#           villain="raana",
#           support_role="satyaraj",
#           second_heroine="Thamanna")

#whenevr u dont know sequence and count of args/params, then we can go with
#these arbitrary keyword args(**x).
#it will take the values in the form of dictionary

#lambda function is used to perform simplest task with very short form
# of the function definition

# rules to be follow for lambda:
# 1.use lambda keyword
# 2.no need of function name and def keyword and ()
# 3.lamda function defintion should be written in sinle line only
# 4.here no need of using return keyword, 
# by default lambda function can return value itself.

#a function without name can be called as anonymous
#so in lambda we will use that anonymous function only

def sample():
    return "hello"
sample()

# op=lambda:"hello" #lamda function which is returning "hello"

# print(op())

# op=lambda:print("hii, welcome") 
#lambda function which prints "hii, welcome" but not returning anything
# print(op())

# def sample1():
#     print("hello")
#     return "hii"



# def demo(x,y):
#     return x+y
# demo(4,5)

add=lambda x,y:x+y 
#lambda function taking 2 params and performing addition and returning
# the same without return keyword
print(add(4,5))


# def func1(x):
#     return func2()

#func1 is returning another function i.e, func2()
#func1 can take another func as a parmeter also.

#like this, if any function can take another function as a parameter or
#returns another function. then that function can be called as a
#higher-order function


def sample(x):
    print(x)

# sample(sample1())
#whenever we pass a function as a argument into the another function,
#then that passing function can be called as a callback function

#these two higher order and callback functns can comes under the category of
#first-class functions