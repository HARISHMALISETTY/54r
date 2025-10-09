import random
import json

def signUp():
    with open("../data/data.json","r") as f:
        username=input("enter username : ")
        email=input("enter email : ")
        password=input("enter password :")
        user_id=generateUserId(username)
        user_info={
            "user_id":user_id,
            "username":username,
            "email":email,
            "password":password
            }
        print(f"ur userid is {user_id}")
        users=json.load(f)
        users["users"].append(user_info)
    with open("../data/data.json","w") as f:
        json.dump(users,f)
        print("signup is done")
        
def generateUserId(username):
    user_id=username[0:3]+str(random.randint(9999,99999))
    return user_id
def login():
    user=input("enter userid or email : ")
    password=input("enter password : ")
    with open("../data/data.json","r") as f:
        users_data=json.load(f)       
        users_info=users_data["users"]
        for x in users_info:            
            if ((user==x["user_id"]) or(user==x["email"])and password==x["password"]):
                print('login successfull')
                break
        else:
                print("invalid credentials")
                
        
