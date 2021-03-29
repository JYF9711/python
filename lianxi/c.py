import os
f=open("./text/a.txt",'r')
content=f.read(5)
print(content)
print("-"*30)
content=f.read()
print(content)
f.close()
