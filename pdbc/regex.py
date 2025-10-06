#regex is a one of the advanced data type

# regular expressions

#length atleast 7-9
#1 uc,1 lc,1 sc,1num..
#starts with specfic word
#ends with specific word
#that should not contain our name


#harish123@@

#email--->@gmail.com
#match,search,findall methods in regex

# i/p should match with our ownformat(using regex)

# regex=r"hello"
# ip="world hello hi some hello"

# import re 

# x=re.findall(regex,ip)
# print(x)

import re
# regex=r"hello"
# ip="world hello hello "
# op=re.match(regex,ip)
# print(op)
# if(op):
#     print("valid input")
# else:
#     print("invalid input")

#.
# regex=r"h.t"
# op=re.match(regex,"hi3t")
# print(op)

# #^
# regex=r"^HDFC|hdfc"
# op=re.match(regex,"hdfcs12345")
# if(op):
#     print('valid input')
# else:
#     print('invalid input')

#$
#only the inputs which will ends with xyz only accepted here
# regex=r"xyz$"
# op=re.search(regex,"abcxyz")
# if(op):
#     print('valid')
# else:
#     print('invalid')

#/d
# regex=r"^hdfc\d+$"
# op=re.search(regex,'hdfc12345')
# if(op):
#     print('valid')
# else:
#     print('invalid')

#[]

# regex=r"[a-eA-F3-7]"
# op=re.search(regex,"012")
# if(op):
#     print('valid')
# else:
#     print('invalid')



#()
# regex=r"(dev)"
# op=re.search(regex,"harish-developer")
# if(op):
#     print('valid')
# else:
#     print('invalid')

# #{}
# {5}-->should have exactly length5
# {5,}-->min length is 5 
# {5,10}--->min:5 and max is 10

#pancard validation

#first 5 uppercase alphabetes
#second 4 any numbers
#ends with single uppercase alphabet

# regex=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"

# pc1="OKLHJ3089Q"

# regex=r"^(\+91)\s[6-9]{1}[0-9]{9}$"
# ip="+91 6895412305"
# op=re.search(regex,ip)
# if(op):
#     # print('valid pancard')
#     print('valid mble num')
# else:
#     print('invalid mble num')




# regex=r"^[1-9]{1}[0-9]{5}$"
# ip="524005"

# op=re.search(regex,ip)
# if(op):
#     print('valid pincode')
# else:
#     print('invalid pincode')


'2025-09-26'
regex=r"[0-9]{4}-[0-9]{2}"
#mnth-->should starts with 0 or 1
# if starts with 0 then should ends with 1-9
# if starts with 1 then should ends with 0-2

# date-->length should be 2
#starts with 0 then ends with 1-9
# starts with 1 and 2 then ends with 0-0 
#starts with 3 then should ends with (0-1)




