import os

f=open("./text/a.txt",'r')
content=f.readlines()
print(type(content))
i=1
for tmp in content:
    print("%d:%s"%(i,tmp))
    i+=1
f.close()
