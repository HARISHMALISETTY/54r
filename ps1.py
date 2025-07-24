# list1=["hello","some","python","java"]

# for x in list1:   
#     rev=""
#     for y in range(len(x)-1,-1,-1):        
#         rev+=x[y]
#     print(rev)

# ip=[123,456,789,146,9801]
# op=[321,654,987,641,1089]
# *
# **
# ***
# ****
# *****



# n=5
# for row in range(1,n+1): 
#     rows="" 
#     for cols in range(1,row+1):
#         rows+="*"
#     print(rows)

# n=5
# for row in range(1,n+1): 
#     rows=0 
#     for cols in range(1,row+1):
#         rows=rows*10+cols
#     print(rows)

# 1
# 12
# 123
# 1234
# 12345

# n=5
# for row in range(1,n+1): 
#     rows=0 
#     for cols in range(1,row+1):
#         rows=rows*10+row
#     print(rows)
# 1
# 22
# 333
# 4444
# 55555

# n=5
# for row in range(1,n+1): 
#     rows="" 
#     for cols in range(1,row+1):
#         rows+=chr(97+cols-1)
#     print(rows)
# a 
# ab 
# abc 
# abcd
# abcde
# n=5
# for row in range(1,n+1): 
#     rows="" 
#     for cols in range(1,row+1):
#         rows+=chr(97+row-1)
#     print(rows)
# a
# bb
# ccc
# dddd
# eeeee

# name="harish"
# op=""
# for x in name: #h a r
#     op+=x #har
#     print(op)
    #h
    #ha
    #har

# h 
# ha 
# har 
# hari 
# haris
# harish

# *****
# ****
# ***
# **
# *

# for x in range(5,0,-1):
#     str1=""
#     for y in range(1,x+1):
#         str1+="*"
#     print(str1)

list=["hi","hello","hi","hello","some","thing"]
dict={}

for char in list:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1

print(dict)
# op={"hi":2,"hello":2,"some":1,"thing":1}

str1="BANANA"
op={"B":1,"A":3,"N":2}