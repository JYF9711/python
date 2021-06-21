list=[11,22,33,44,55,66,77,88,99,123,124,335,667]
x=int(input("请输入："))
#x=1235436
left=0
right=len(list)-1
while left<right:
    mid=(right+left)//2
    if list[mid]==x:
        break
    elif x<list[mid]:
        left=mid-1
    else:
        right=mid+1
if left<=right:
    print("找到了 ，第%d个数是%d。"%(mid+1,x))
else:
    print("不再表里")
