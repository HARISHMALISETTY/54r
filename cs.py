# statements which executes based on a specific condition,
# then it can be called as conditional statements

#these can be use for decision making purpose

#we have multiple types in conditional statements:

# 1.simple-if 
    # statements will executes whenever condition is true only
# 2.if-else
    # whenever we want to execute one more statement as a alternate if true statement 
    # doesn't executes
    # for running false statement, we can use else . 
# 3.nested-if 
# 4.elif 
# 5.terinary operator

# print("hello world")
a=10
b=16

# if(a+b==25):
#     print("welcome")
# if(a+b<=30):
#     print("hii")
# if(a+b>=20):
#     print("hellooo")

# "maheshbabu","pspk","AA","NTR","Prabhas"
# Mb_Contact=True 
# Pspk_Contact=True
# AA_Contact=True
# Ntr_Contact=False
# Prabhas_Contact=False
# Mb_will_Answer=True
# Pspk_will_Answer=False
# AA_will_Answer=True
# Ntr_will_Answer=True
# Prabhas_will_answer=True

# if(Mb_Contact and Mb_will_Answer):
#     print("i can call to Maheshbabu")
# if(Pspk_Contact and Pspk_will_Answer):
#     print("i can call to pspsk")
# if(AA_Contact and AA_will_Answer):
#     print("i can call to AA")
# if(Ntr_Contact and Ntr_will_Answer):
#     print("i can call to Ntr")
# if(Prabhas_Contact and Prabhas_will_answer):
#     print("i can call to prabhas")  

# Mb_contact=False
# if(Mb_contact):
#     print("can call to MB")
# else:
#     print("call to his PA")

# num=52
# if (num%2==0) :
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# num=125289
# if(num & 1 ==0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd") 


#in operator
# num=125012589
# cnvrt=str(num)
# # print(cnvrt[-1])

# seq=[0,2,4,6,8]
# if(int(cnvrt[-1]) in seq):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# seq="02468"

# num=1254589
# ld=num%10

#nested if-->if inside if

# if(condition):
#     if(condition):
#         print()
#     else:
#         print()
# else:
#     print()

# 1.login--->-->user-->welcome to user 
#            ---> invalid user 

# ---->please login

is_login=True
login_role="user"

# if(is_login):
#     if(login_role=='user'):
#         print("welcome to user")
#     else:
#         print("invalid user")
# else:
#     print("please login")

# num=-25
# if(num>0):
#     print("u have entered positive number")
#     if(num%2==0):
#         print("num is even")
#     else:
#         print("num is odd")
# else:
#     print("u have entered negative num please enter positive")
    
# is_login=True
# user_role="delivery_boy"

# if(is_login):
#     if(user_role=='customer'):
#         print("access customer app")
#     if(user_role=='delivery_boy'):
#         print("access delivery boy app")
#     if(user_role=='rest-owner'):
#         print("access restrnt app")
# else:
#     print("please login")



# if(is_login):
#     if(user_role=='customer'):
#         print("access customer app")
#     elif(user_role=='delivery_boy'):
#         print("access delivery boy app")
#     elif(user_role=='rest-owner'):
#         print("access restrnt app")
# else:
#     print("please login")




#   1.rank<10000--->JNTUH
#   2.10000<rank<25000--->Mallareddy
#   3.25000<rank<50000---->vignan 
#   4.rank>50000--->local college
#   5.fail--->go and join in b.com/b.sc


rank=15250
# if(rank<10000):
#     print("JNTUH")
# if(rank>10000 and rank<25000):
#     print("Mallareddy")
# if(rank>25000 and rank<50000):
#     print("Vignan")
# if (rank>50000):
#     print("local college")
# if(rank==0):
#     print("go and join in degree college")
# if(rank>0 and rank<10000):
#     print("JNTUH")
# elif(rank<25000):
#     print("mallareddy")
# elif(rank<50000):
#     print("vignan")
# elif(rank>50000):
#     print("local college")
# else:
#     print("go and join degree college")

percentage=150
if(percentage<0 or percentage>100):
    print("invalid percentage")
elif(percentage>=90):
    print("grade -A")
elif(percentage>=80):
    print("grade-B")
elif(percentage>=65):
    print("grade -c")
elif(percentage>=45):
    print("grade-D")
else:
    print("fail")



#ATM SIMULATOR
# 1.if withdral amnt is greater than balance--->then show insufficient balance
# 2.if withdral amnt is less than balance-->
#     if withdrawl amnt is multiples of 100--->then withdrawl success
#                                     else--->withdrawl amnt should be multiples of 100 only


# #
# if user knows-->F.E-->become-->F.DEV 
#              -->B.E-->become ->B.Dev
#              -->D.B-->become ->D.dev
#              -->F.E AND B.E AND D.B-->F.S.DEV
#              -->dont know anything-->go and learn skills


#.terinary operator


