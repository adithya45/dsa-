def linearsearch(arr, target, size):
    if size == 0:
        return -1
    elif arr[size-1] == target:
        return size-1
    else:
        return linearsearch(arr, target, size-1)
    
a=int(input ("enter the length of list:"))
list=[]
for i in range(a):
    list.append(int(input("enter a number:")))
target=int(input("enter a number to search:"))

print (linearsearch(list , target, len(list)-1 ))