# with open("../demo.txt",'w') as f:
#     f.write("hello world")
#     with open("./demo.txt",'r') as g:
#         g.read()

import os

# os.remove('./demo.txt') #we can delete directly the file if it exists

if (os.path.exists('./demo.txt')):
    os.remove('./demo.txt')
else:
    print("file is not avaialable")