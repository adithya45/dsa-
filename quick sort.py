#Quick sort
def part(arr,low,high):
    pivot=arr[low]
    l=low+1
    r=high
    while True:
        while l<=r and arr[l]<=pivot:
            l=l+1
        while l<=r and arr[r]>=pivot:
            r=r-1
        if l<=r:
            arr[l],arr[r]=arr[r],arr[l]
        else:
            break
    arr[low],arr[r]=arr[r],arr[low]
    return r 
def sort(arr,first,last):
    if(first<=last):
        x =part(arr,first,last)
        sort(arr,first,x-1)
        sort(arr,x+1,last)
    return arr
arr=[]
a=int(input("Enter number of elements: "))
for i in range(a):
    arr.append(int(input("Enter number: ")))
sort(arr,0,len(arr)-1)
print(arr)