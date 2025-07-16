# num1=795423
# num=str(num1)
# 3
# 2
# 4
# 5
# 9
# 7

# for x in range(len(num)-1,-1,-1):
#     print(num[x])


# num=789
# ld=num%10 #9
# print(ld) #9
# num=num//10 #78
# ld=num%10 # 8
# print(ld) #8
# num=num//10 #7
# ld=num%10 #7
# print(ld) #7
# num=num//10


# num=54789
# while(num>0): #true #true #true #true #true
#     ld=num%10 #9 #8 #7 #4 #5
#     # print(ld)  #9 #8 #7 #4 #5
#     num=num//10 #5478 #547 #54 #5 #0
# print(num)

# num1=5
# num2=6
# print(num1+num2)


# 5*10+6=56

# 56,7
# 56*10+7=567

#reverse given num
# num=254521
# num1=num
# rev=0
# while(num>0): #true #true #true #true #true
#     ld=num%10 #9 #8 #7 #4 #5
#     rev=rev*10+ld #0*10+9==>9 #9*10+8==>98 #98*10+7==>987 #987*10+4==>9874 #9874*10+5==>98745
#     num=num//10 #5478 #547 #54 #5 #0
# print(rev)

# if(num1==rev):
#     print("its a palindrome")
# else:
#     print("not a palindrome")

#find the sum of the digits for a given num without string conversion
num=12548
# op=1+2+5+4+8
# sum=0
# while(num>0):
#     ld=num%10
#     sum+=ld
#     num=num//10
# print(sum)

#find the sum of the square of digits for a given num without string conversion

# sum=0
# while(num>0):
#     ld=num%10
#     sum+=ld**2
#     num=num//10
# print(sum)

#find length of the given num or count the digits in given num without string conversion
# num=12456
# count=0
# while(num>0):
#     ld=num%10
#     count+=1
#     num=num//10
# print(count)


#armstrong number
# 12345
# 1^5+2^5+3^5+4^5+5^5=12345

# 153
# 1^3+5^3+3^3=153 


num=153
num1=num
num2=num
len=0
while(num>0):
    ld=num%10
    len+=1
    num=num//10
print(len)

sum=0
while(num1>0):
    ld=num1%10
    sum+=ld**len
    num1=num1//10
print(sum)

if(sum==num2):
    print("it is a armstrong")
else:
    print("not a armstrong num")

#find factors for given number
#check num is perfect num or not
#check num is perfect square or not
#check num is neon or not
#check num is sunny or not