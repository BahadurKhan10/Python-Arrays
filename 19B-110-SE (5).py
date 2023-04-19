#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None


# In[82]:


class SatelliteData:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtFront(self, e):
        New=Node(e)
        x = self.head
        if self.head==None: 
            self.head=New
            self.tail = New
        else:
            New.next = x
            self.head = New

   
    def RemoveFront(self):
        cou = self.head
        if cou == None:
            print("List is Empty")
        else:
            x = self.head.next
            self.head = x
            cou.value = None

    
    def InsertAtEnd(self, e):
        new = Node(e)
        cou = self.tail
        if self.head == None:
            self.head = new
        else:
            cou.next = new
            self.tail = new
       
    def RemoveAtEnd(self):
        x = self.head
        while x.next != None:
            x = x.next
            self.tail = x
            self.tail.next = None
        if x==None:
            print("List is Empty")


    def Get(self, i):
        cou = None
        while self.head:
            if cou == i:
                return self.head.value
            cou += 1
            self.head = self.head.next

    def GetAll(self):
        while self.head:
            return self.head.value
            self.head = self.head.next


# In[92]:


class SatelliteUtility:
    def _init_(self, filename):
        self.filename = filename
        self.satellites = []
        self.al= []

    def ReadData(self): #Problem raises when i try to access the file
        file = open(self.filename) #Accessing file
        self.al = (file.read()).split("\n") #Reading through lines
        file.close() #Closing file
        print("ReadData:",self.al) #Printing the data which is read

    def ProcessData(self):
        self.ReadData() #Calling the ReadData function
        for line in self.al: 
            sat = SatelliteData(line[0], line[2]) #Pointing at these postions
            sat.InsertAtFront(line[4]) #Inserting font at specific line
            sat.InsertAtEnd(99) #inserting at end
            sat.GetAll() 
            sat.RemoveAtEnd()
            sat.GetAll()           #These are above functions in Satellite class
            sat.RemoveFront()
            sat.GetAll()
            self.satellites.append(sat)

    def GetSummary(self):
        x = [] #Empty list
        satellites=[] #Emppty list
        for sat in self.satellites:
             x.append((sat.satellite, sat.Count())) #Getting the whole summary of Data which is processed
        return x


# In[93]:


x = SatelliteData()
x.InsertAtFront(4)
x.InsertAtFront(3)
x.InsertAtFront(2)
x.InsertAtFront(1)


# In[94]:


x.RemoveFront()
x.GetAll()


# In[95]:


x.RemoveAtEnd()
x.GetAll()

