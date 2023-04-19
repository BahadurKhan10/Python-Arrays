#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def InsertatFirst(self,value):
        newnode = Node(value)
        x=self.head
        if x is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head= newnode
            
    def Print(self):
        x=self.head
        while x:
            print(x.value)
            x=x.next
            
    def InsertatEnd(self, value):
        newnode = Node(value)
        x=self.tail
        if x is None:
            self.head=newnode
            self.tail=newnode
        else:
            x.next=newnode
            newnode.next=None
            self.tail=newnode
            
    def InsertAfter(self, item, value):
        h = self.head
        while h != None:
            if h.value == item:
                n = Node(value)
                n.next = h.next
                h.next = n
                break
            h = h.next
            
    def DeleteAtFirst(self):
        x=self.head
        x=x.next
        self.head.next=x
        
    def DeleteAtEnd(self):
        if self.head == None:
            print("List is empty")
        h = self.head
        while h.next.next != None:
            h = h.next
        self.tail = h
        self.tail.next = None
    
    def DeleteByValue(self, value):
        h = self.head
        
        while h.next != None:
            if h.next.value == value:
                removed = h.next
                h.next = h.next.next
                removed.next = None
                del removed
                break
            h = h.next            


# In[18]:


obj=LinkedList()
obj.InsertatFirst(1)
obj.InsertatFirst(5)
obj.InsertatEnd(2)
obj.InsertatEnd(9)
obj.InsertatFirst(0)
obj.InsertatFirst(88)
obj.DeleteByValue(2)
obj.DeleteAtEnd()
obj.DeleteAtFirst()
obj.InsertAfter(2,5)
obj.Print()

