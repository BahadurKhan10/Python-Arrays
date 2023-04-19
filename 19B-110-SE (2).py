#!/usr/bin/env python
# coding: utf-8

# # A

# In[18]:


def LinearSearch(List, Value):
    res = 0
    for x in List:
        if x == Value:
            return res
        res += 1
    return -1
    
A = [11,12,13,14,15,16]
print(LinearSearch(A, 14))


# # B

# In[22]:


def BinarySearch(List,n, Value): 
    count = 0
    for i in List: 
        if (i == Value): 
            count = count + 1
    return count
data = [1,2,2,3,4,5,6,7,8,4,4,3]
n = len(data)
print(BinarySearch(data, n, 4))


# # C

# In[45]:


class List:
    def __init__(self):
        self.lst = []
        
    def printList(self):
        return self.lst
    
    def InsertAtFirst(self, value):
        self.lst = [value]+self.lst
        
    def InsertAtEnd(self, value):
        self.lst = self.lst+[value]
    
    def DeleteFromFirst(self):
        a = self.lst[-1]
        self.lst = self.lst[:-1]
        return a
    
    def DeleteFromEnd(self):
        a = self.lst[-1]
        self.lst = self.lst[:-1]
        return a
    
    def LinearSearch(self, Value):
        count = 0
        for i in self.lst:
            if i == Value:
                return count
            count += 1
        return -1
       
    def BinarySearch(self, value):
        n = len(self.lst)
        L = 0
        R = n-1
        while L <= R:
            m = ((L + R) // 2)
            if (self.lst[m] < value):
                L = m+1
            elif (self.lst[m] > value):
                R = m-1
            else:
                return m
        return -1

    def IsSorted(self):
        x=len(self.lst)
        a=self.lst
        for i in range(x-1):
            if a[i]> a[i+1]:
                return False
        return True
    
    def Search(self, value):
        if (self.IsSorted()):
            return self.BinarySearch(value)
        else:
            return self.LinearSearch(value)


# In[50]:


myList = List()
myList.InsertAtFirst(22)
myList.InsertAtFirst(42)
myList.InsertAtEnd(70)

print("Before List: ",myList.printList())
print("Deleted at first:",myList.DeleteFromFirst())
print("After List: ",myList.printList())

myList.InsertAtFirst(0)

print("Deleted from end:",myList.DeleteFromEnd())
print("Linear Search 22:",myList.LinearSearch(22))

myList.InsertAtEnd(10)

print("Binary Search 10:",myList.BinarySearch(10))
print("Is "+str(myList.printList())+" sorted?",myList.IsSorted())
print("Find 42 in linst:",myList.Search(42))

myList.InsertAtEnd(99)

print("Fin 99 in list:",myList.Search(99))


# In[ ]:




