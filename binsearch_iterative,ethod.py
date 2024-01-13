a=int(input ("enter the length of list:"))
list=[]
for i in range(a):
    list.append(int(input("enter a number:")))

def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

list=selectionsort(list)

flag =0
l=0
h=len(list)-1
key=int(input("enter the number to search:"))
while l<= h:
    mid=(l+h)//2
    if list[mid]==key:
        flag=1
        break
    elif list[mid]>key:
        h=mid-1
    else:
        l=mid+1
if flag ==1:
    print("element found at position",mid+1)
else:
    print("element not found") 