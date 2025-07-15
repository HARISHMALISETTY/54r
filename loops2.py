# terinary operator
# applying loops for sequence data types
# break and continue statements
# terinary operator is simliar to if-else.
# print("tru statement")if True else print("false statement")
# if(True):
#     print("true statement")
# else:
#     print("false ")
# x=20 if False else 40
# print(x)
#we can use terinary operator for simple and short conditions based operations
#we can assign value to a variable based on the condition using terinary operator
# syntax: Truestatement if True else False statement
# islogin=False
# print("login successful") if islogin else print("login failed")
# a=4
# b=5
# print("a is largest") if a>b else print ("b is largest")
# user="user"
# role="admin-role" if user=="admin" else "employee-role"
# print(role)

#break and continue

# for x in range(1,10): #1 2 3 4 5 6 7 8 9 
#     print(x)
#     if(x==5):
#         continue
#     print(x,"hii")
    
# for x in range(1,10): #1 2 3 4 5
#     print(x)
#     if(x==5):
#         break
#     print(x,"hii")


# str="welcomehello"

# print(str[len(str)-1])

#to print characters from reverse direction
# for x in range(len(str)-1,-1,-1):
#     print(str[x])

# for x in range()


# str="7894563240"
# print(str[0])
# print(str[1])
# print(str[2])
# for x in str: #by default this will iterates every character in the string from start to end
#     print(x)

# for x in range(3,9):
#     print(str[x])

# for x in range(0,len(str)):
#     print(str[x])



# str1="hello"
# str1="MADAM"
# str2=""
# #op=olleh without using end=""
# for x in range(len(str1)-1,-1,-1): # 4 3 2 1 0
#     # print(x)
#     str2+=str1[x] # str2+=str1[2] #olleh
#     # print(str1[x])
# print(str2)
# if(str1==str2):
#     print("it is a palidrome")
# else:
#     print("not a palindrome")

# list1=["so","and","are","we","hello",458,879,"ok","hi"]

# for ele in list1:
#     print(ele)

# for ele in range(len(list1)-1,-1,-1):
#     print(list1[ele])

list1=["h","e","l","l","o"]

#op=_h_e_l_l_o

op=""
# for x in list1:
#     op+=f"_{x}"
# print(op)

#o_l_l_e_h_

# for x in range(len(list1)-1,-1,-1):
#     op+=f"{list1[x]}_"

# print(op)


ip="SOMETHING"
OP="_S-O_M-E_T-H_I-N_G"
