def selectionsort(list):
    a=len(list)
    for i in range(a):
        min_index = i
        for j in range(i+1,a):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

a=int(input ("enter the length of list:"))
list=[]
for i in range(a):
    list.append(int(input("enter a number:")))
list=selectionsort(list)

key=int(input("value to search:"))

l=0
h=a-15
result=binary_search(list,key,l,h)
if result== -1:
    print("element not found")
else:
    print("element found at index",result)    