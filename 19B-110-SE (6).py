#!/usr/bin/env python
# coding: utf-8

# In[12]:


class BST:
    def _init_(self):
        self.root = None
        
    def Insert(self, value):
        self.root = self.__Insert(self.root, value)
    def __Insert(self,x,value):
        if x == None:
            x = Node(value)
        else:
            if value<x.value:
                
                x.left = self.__Insert(x.left,value)
            else:
                x.right = self.__Insert(x.right, value)
        return x
    
    
    def InOrder(self):
        return self.__InOrder(self.root)
    def __InOrder(self, x):
        if x:
            self.__InOrder(x.left)
            print(x.value)
            self.__InOrder(x.right)
    
    def PreOrder(self):
        return self.__PreOrder(self.root)    
    def __PreOrder(self, x):
        if x:
            print(x.value)
            self.__PreOrder(x.left)
            self.__PreOrder(x.right)
            
            
            
    def PostOrder(self):
        return self.__PostOrder(self.root)
    def __PostOrder(self, x):
        if x:
            self.__PostOrder(x.left)
            self.__PostOrder(x.right)
            print(x.value)
    
    def Print(self):
        if self.root!=None:
            self.__Print(self.root)

    def __Print(self,current_node):
        if current_node!=None:
            self.__Print(current_node.left)
            print (str(current_node.value))
            self.__Print(current_node.right)

