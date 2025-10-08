import json 

# ip=['apple','banana','grapes']

# # with open('data.json','w') as f:    
# #     # f.write(json.dumps(ip))    
# #     json.dump(ip,f) 

#     # dumps--->only converts to json 
#     # dump---->json conversion and stores in file 

# with open('data.json','r')as f:
#     # data=f.read()
#     # convrt_data=json.loads(data)
#     # print(data[2])
#     # print(convrt_data[2])
#     data=json.load(f)
#     print(data[1])

#     # read then loads 

#     # load 
# ip1='pineapple'
# with open ('data.json') as f:
#     data=json.load(f) #data will change from json string to list
#     if ip1 not in data["fruits"]:        
#         data["fruits"].append(ip1) #new element will append into the list
#     else:
#         print(f'{ip1} already exists')

# with open('data.json','w') as f:
#     json.dump(data,f)
#     print('data updated successfully')
user=input("enter user name")
file_name='data.json'
#remove operation only for authorised persons
# remove_element=input("enter fruit name")
# with open(file_name,'r') as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if remove_element not in data["fruits"]:
#             print(f"{remove_element} is not available")
#         else:
#             data["fruits"].remove(remove_element)
#             print(f"{remove_element} is removed successfully")
#     else:
#         print("u r not authorised to perfrom remove operation")
# with open(file_name,'w')as f:
#     json.dump(data,f)

#adding operation only for authorised persons
adding_element=input("enter fruit name to be add : ")
with open(file_name,'r') as h:
    data=json.load(h)
    if user in data["users"]:
        if adding_element in data["fruits"]:
            print(f"{adding_element} is already exists")
        else:
            data["fruits"].append(adding_element)
            print(f"{adding_element} is added successfully")
    else:
        print("u r not authorised to perfrom adding operation")
with open(file_name,'w')as f:
    json.dump(data,f)






