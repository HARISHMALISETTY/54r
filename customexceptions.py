# try:
#     x=int(input('enter a value:'))
#     print(x)
#     if x<0:
#         raise NameError('negative numbers not allowed')
    
# except ValueError:
#     print('error occured')
# except NameError as e:
#     print(e)


# try:
#     age=int(input('enter age:'))
#     if age<18:
#         raise TypeError('childrens are not allowed')
#     elif(age>40):
#         raise ValueError('uncles are not allowed')
# except ValueError as e:
#     print(e)

#here iam defining errors with inbuild errormethods by giving my customised message
#if user breaks my rules.

#valueerror, nameerror,typerror..
#userValidateError

class userValidateError(Exception):
    pass
class myError1(Exception):
    pass 
class myError2(Exception):
    pass 

user={'name':'harish','password':'harish123'}
try:
    ip1=input('enter username :')
    ip2=input('enter password :')
    if(ip1 not in user.values()):
        raise userValidateError('invalid credentials')
    else:
        print('login succeassfull')
except userValidateError as e:
    print(e)




