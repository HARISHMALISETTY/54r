import json
from auth import signUp
from auth import login

def start():
    ip=int(input("enter choice : "))
    if ip==1:
        signUp()
    elif ip==2:
        login()
    else:
        print("invalid input")        

start()


