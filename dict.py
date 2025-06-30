# dict={property1,property2,property3,...}
# dict={"key1":value1,"key2":value2,"key3":value3}
# bike_info={
#     "bike_name":"Pulsar",
#     "price":95000,
#     "colors":["red","black","blue"],
#     "model":["Ns-150","rs-200","220f","150-dts"],
#     }
# print(bike_info)
#how to add one more property in existing dictionary

# bike_info["key"]=value 
# bike_info["ABS"]=True # adding abs property into the existing dictionary
# bike_info["price"]=100000 #updating price of the bike
# print(bike_info["colors"]) #accessing colors property from the dictionary
# print(bike_info["colors"][1])
# print(bike_info)

#define a dictionary with student information
# 1.name , 2.gender, 3.age, 4.skills,5.highestqualification,6.address

stud_info={}
stud_info["name"]="kiran kumar"
stud_info["gender"]="male"
stud_info["age"]=22
stud_info["skills"]=["html","css","js","python","react","sql"]
stud_info["highest_qual"]="B.tech"
stud_info["address"]={"d-no":'3/9/258',
                      "street":"james garden",
                      "village":"kukatpalli",
                      "city":"hyderabad",
                      "pincode":500085}
stud_info["name"]="M kiran Kumar"
stud_info["skills"]=stud_info["skills"]+["nodejs"]

del stud_info["gender"] #deleting the gender property from the dictionary


print(stud_info)
