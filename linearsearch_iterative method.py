a=int(input('enter the length of list:'))
list=[]
for i in range(a):
    list.append(int(input("enter a number:")))
flag=0
key=int(input("enter a number to search:"))
for i in range(len(list)):
    if list[i]== key:
        flag=1
        break

if flag==1:
    print("the number",key,"is found at",i+1,"postition")

else:
    print(key,"is not found in the list")
