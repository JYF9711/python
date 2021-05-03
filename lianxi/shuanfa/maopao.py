# def bubbleSort(arr):
#     for i in range(1,len(arr)):
#         for j in range(0,len(arr)-i):#保留最后一个最大的数
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 # print(arr)
#
#         # print(arr)
#     return arr
# arr=[12,32,22,14,41,33,23]
# print(bubbleSort(arr))
def bubble(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[12,32,22,14,41,33,23]
print(bubble(arr))