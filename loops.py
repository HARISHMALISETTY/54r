# for x in range():
#     print(x)

# range(10)# arg will consider as ending range which is exclusive
#starts at 0 and ends before 10

# range(2,10) #
# frst arg-->starting range 
#second arg-->range ends before it

# range(1,10,2)


# 0 1 2 3 4 5 6 7 8 9 -->range(10)
# 2 3 4 5 6 7 8 9---->range(2,10)
# 1,3,5,7,9------->range(1,10,2)

# for x in range(10):


# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)


# for x in range(10):
#     print(x)


# for x in range(5):
#     print("hello")


# x=5
# # x+=1
# # x+=1
# # x+=1
# # x+=1
# # x+=1
# for i in range(5):
#     x+=1
# print(x)

# str="hello"

# for i in range(1,10,3):
#     str+="hi" 
#     print(str) 

# for x in range(1,11):
#     print(f"2X{x}={2*x}")

# def mul(num):
#     for x in range(1,11):
#         print(f"{num}X{x}={num*x}")

# mul(15)


# 1 to 10 range(1,11)
# 10 to 1 range(10,0,-1)

# for x in range(10,0,-1):
#     print(x)


# we know how to print from 1 to 10
# sum of all numbers from 1 to 10
# 1+2+3+4+5+6+7+8+9+10

# sum=0
# for x in range(1,11):
#     sum+=x
# print(sum)

#sum of squares of frst 10 numbers
# sum=0
# for x in range(1,11):
#     sum+=x**2
# print(sum)


# from range of 1 to 21
# if num is divisible by 3 then print num fizz
# if num is divisible by 5 then print numbuzz
# if num is divisible by both 3 and 5 then print num fizzbuzz


for x in range(1,20):
    if(x%3==0 and x%5==0):
        print(f"{x} -fizz buzz")
    elif(x%5==0):
        print(f"{x} - buzz")
    elif(x%3==0):
        print(f"{x} - fizz ")
    else:
        print(x)

#print all even numbers from 40 to 20 in rev order
#print all odd numbers from 30 to 10 in rev order
#find sum of squares of all odd numbers from 1 to 20
#find sum of all even numbers from 20 to 40

