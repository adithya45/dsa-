def merge_sort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left_half=list[:mid]
    right_half=list[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    sorted_list=merge(left_half,right_half)
    return sorted_list

def merge(left,right):
    a=[]
    l,r=0,0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            a.append(left[l])
            l+=1
        else:
            a.append(right[r])
            r+=1
    a.extend(left[l:])
    a.extend(right[r:])
    return a        
list=[64, 34, 25, 12, 22, 11, 90]

sortedlist=merge_sort(list)
print(sortedlist)