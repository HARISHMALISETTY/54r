
#errors-->compiletime,runtime
#compiletime--->
#code won't compiles completely,due to mistake in syntax.
#compilation will stops.

#runtime-->errors which occurs after compilation and during runtime, before displaying
#the output.
#this will occurs due to some wrong inputs and wrong logic.

# if True
#     print("hello")
#here this code never compile due to syntax issue.this can be considered as compiletime error.

# x=4
# y='harish'
# sum=x+y 
# print(sum)
#this code will throw error after compilation and before performing operation and 
#displaying the output.
#this can be considered as a runtime error.
# try:
#     x=int(input('enter x value: '))
#     y=int(input("enetr y value: "))
#     sum=x+y 
#     print(sum)
# except:
#     print('error occured')


#try:
    #ip=int(input('enter input value: '))
    #print(ip)
#except:
 #   print('some error occured')

#finally:
 #   print('execution completed') 


#zerodivision error

# try:
    
# except:
# try:
#     ip=int(input('enter value:'))
#     print(ip/0)
# except ValueError as e:
#     print('give only numbers not strings')
# except ZeroDivisionError as e:
#     print('we cant divide by zero')
# except TypeError as e:
#     print('we cant do division for string',e)
# except:
#     print('some unknown error occured')

# try:
#     ip=4
#     ip.append(5)
# except:
#     print('method is not applicable')


# try:
#     ip=[4,7,9,2]
#     print(ip[6])
# except IndexError:
#     print('index is out of range')

# try:
#  x=5
#  y=7
#  z=8
#  print(a)
# except IndentationError:
#     print('indentation is not proper')
# except TypeError:
#    print('invalid type which does not support')
# except NameError:
#    print('variable is not declared and intialized with any value yet')
# except:
#    print('something went wrong')
   

# try:
#     open('./hello.txt','r')
# except FileNotFoundError:
# #     print('file is not available in current project')
# try:
#     import some 
# except ModuleNotFoundError:
#     print('it is a invalid module')