#to add data in json dump()
#to read data from json file.
# load()

#eariler we have performed crud operations on text data.so no need of json there
#now i want to perform crud operations on data structures like list,tuple,dictionaries.
#we cant directly perform on them using files.so we need to store data in json format.
# for easy communication and for easy manipulation
#we will perfrom json methods only on objects/dictionaries


import json
# data={'name':'john','age':24,'gender':'male'}
# op=json.dumps(data) #used to convert as a json object

# data1=['hello','hie','welcome']
# op1=json.dumps(data1) #cnvert to json object
# print(type(op1))
# op2=json.loads(op1) #cnvert to its original form
# print(type(op2))

# print(data1[2])
# print(op1[2])
# print(data['name'])
# print(type(op))
# with open('products.json','w') as f:
#     json.dump(data,f,indent=4)


# 1.one student info--->obj/dicti
# 2.multiple students data--->list of dic/object.
# while transferring this entire list--->we have to store in json.everything should be 
# enclose in {}

list=['harish','kiran','abdul','vikas']

# with open('products.json','w') as f:
#     data_json=json.dumps(list)
#     f.write(data_json)

with open('products.json','r') as f:
    res=f.read()
    cnvrt_data=json.loads(res)
    print(cnvrt_data[1])

#add few names into the existing list in the file
#remove any name
