
# def sample():
#     x=25 #x is having local scope
#     print(x)

# sample()

# def sample1():
#     print(x)
# sample1()

#so here x can be accessible only inside the sample(),
#because it is local to the sample()
#in sample() it is having local scope.

# x=45 #global scope because it is declared globally.
#it does not have restrictions to any funcion particularly
# def sample1():
#     print(x)

# def sample2():
#     print(x)
# sample1()
# sample2()


# def func1():
#     def func2():
#         x=45 
#         # x is having enclosed scope, we can access it only 
#         # inside the func2 only but not out of func2 and within fun1
#     func2()
#     print(x) # trying to access 'x'
# func1()

# 1.global
# 2.local 
# 3.enclosed

# we can also modify scopes in python using 
# 1.global
# 2.nonlocal 
# these are scope modifiers

# def sample1():
#     global x #here iam declaring x globally from sample1()
#     x=10
# sample1()
# print(x)
# def sample2():
#     print(x)
# sample2()

#with the help of scope modifier global, i changed the x scope from local to global.

# def sample1():
#     x=10
#     def sample2():
#         # nonlocal x
#         x=5
#         print(x)
#     sample2()
# sample1()

#here i am changing x scope from enclosed to nonlocal.

# name="kiran"
# def greet():
#     global name
#     name="kumar"
#     print(f"hello {name}")
# greet()

# print(name)

# x=chr(98)
# print(x)

#98 is ascii value of b
#66 is ascii value of B

# 98-32==>66
# 100-32==>68

# 65+32==>97
# 67+32==>99

# x='D'

# print('A'<x<'Z') #CHECKING WHTHER INPUT IS UPPERCASE OR NOT

# print('a'<x<'z') # checking whther input is lowercae or not


ip_char='k'
asci_value=ord(ip_char)
if('A'<ip_char<'Z'):
    print("it is in uppercase")
    cnvrt=asci_value+32
    print(chr(cnvrt),"converted to lowercase")
elif('a'<ip_char<'z'):
    print("it is in lowercase")
    cnvrt=asci_value-32
    print(chr(cnvrt),"cnvered to uppercase")
else:
    print("invalid character")




# c-->lowercase-->99
# C--->uppercase-->67
# to cnvert into upeercase--->ip_ascii-32--->we will get ascii value of uppercase 

# to cnvert into lowercase--->ip_ascii+32---->we will get ascii value  of lowercase



# ord()--->gives the ascii value of character

# chr()-->get the character as per ascii value


# 'A' AND 'Z'--->input is uppercase
# 'a' and 'z'-->input is lowercase




# input-->c then print next character in uppercase i.e., D 

# input --->D then print prvs character in lowercase i.e., f

