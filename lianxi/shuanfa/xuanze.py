# 选择排序
def selectSort(arr):
    for i in range(len(arr)-1):
        #记录最小数的索引
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
            # if arr[j] < arr[i]:
                minIndex=j
        #i不是最小数时，将i和最小数进行交换
        if i != minIndex:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr
# 冒泡排序
def maopaoSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr


if __name__ =="__main__":
    aaa=[12,32,22,14,41,33,23]
    print(selectSort(aaa))