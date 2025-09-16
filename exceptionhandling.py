
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
try:
    x=int(input('enter x value: '))
    y=int(input("enetr y value: "))
    sum=x+y 
    print(sum)
except:
    print('error occured')