import numpy as np
class hash_table():
    def __init__(self,ms):
        self.ms=ms
        self.array=np.array([-1]*self.ms,dtype='i')
    def lin_probing(self,key,value):
        ind=(key+1)%self.ms
        while ind!=key:
            if self.array[ind]==-1:
                self.array[ind]=value
                break
            else:
                ind=(ind+1)%self.ms
        if ind==key:
            print('hash table is filled')
    #hashing
    def hash(self,value):
        key=value%self.ms
        if self.array[key]==-1:
            self.array[key]=value
        else:
            self.lin_probing(key,value)
    #retrieve
    def check(self,value):
        key=value%self.ms
        if self.array[key]==value:
            print(value,'is present at',key)
        else:
            ind=(key+1)%self.ms
            while ind!=key:
                if self.array[ind]==value:
                    print(value,'is present at',ind)
                    break
                else:
                    ind=(ind+1)%self.ms
            if ind==key:
                print(value,'is not in the hash table')
    #deleting
    def delete(self,value):
        key=value%self.ms
        if self.array[key]==value:
            self.array[key]=-1
            return value
        else:
            ind=(key+1)%self.ms
            while ind!=key:
                if self.array[ind]==value:
                    self.array[ind]=-1
                    return value
                else:
                    ind=(ind+1)%self.ms
    #display
    def display(self):
        for i in self.array:
            print(i,end=' ')
        print('\n')               
if __name__=='__main_':
    ms=int(input('enter maximum size of array::'))
    hata=hash_table(ms)
    print(' ENTER 1 TO INSERT DATA \n ENTER 2 TO CHECK DATA \n ENTER 3 TO DELETE DATA \n ENTER 4 TO DISPLAY HASH TABLE \n ENTER 0 TO EXIT')
    while True:
        v=int(input())
        if v==1:
            hata.hash(int(input('ENTER NO TO INSERT::')))
        elif v==2:
            hata.check(int(input('ENETR NO TO CHECK::')))
        elif v==3:
            a=hata.delete(int(input('ENETR NO TO DELETE::')))
            print(a,'is deleted')
        elif v==4:
            hata.display()
        else:
            break
