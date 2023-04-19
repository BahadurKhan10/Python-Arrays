#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[54]:


class Array:
    def __init__(self,col,row):
        self.col=col
        self.row=row
        self.data=[0 for i in range(self.row*self.col)]

    def Location(self,i,j):
        l=i*self.row+j
        return l
    
    def SetValue(self,i,j,v):
        l=self.Location(i,j)
        self.data[l]=v

    def GetValue(self,i,j):
        l=self.Location(i,j)
        return self.data[l]

    def PrintValue(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(i,j),end=" ")
            print('\n')
            
    def SubValues(self, a1, a2):
        for i in range(self.row):
            for j in range(self.col):
                a1.data[i*self.row+j] -=  a2.data[i*self.row+j] 
        self.PrintValue()

        
    def MultValues(self, a1, a2):
        if a1.col == a2.row:
            result = [0 for i in range(a1.row*a2.col)]
            for i in range((a1.row)): #row of first array
                for j in range((a2.col)): #column of 2nd array
                    for k in range((a2.row)):#for addition while mult
                        result[i*a1.row+j] += a1.data[i*a1.row+k] * a2.data[k*a2.row+j]
            for i in range(a1.row):
                for j in range(a2.col):
                    print(result[i*a1.row+j], end = " ")
                print("\n")
        else:
            print("No of rows & columns of two arrays are not equal")
            
    def Transpose(self):
        result = [0 for i in range(a1.row*a2.col)]
        for i in range(self.row):
            for j in range(self.col):   
                result[j*self.row+i] = self.data[self.location(i,j)]     
        
        for i in range(self.col):
            for j in range(self.row):
                print(result[i*self.row+j], end = " ")

#Driver code is under


# In[55]:


#Setting & Printing value
a1 = Array(3, 3)
a2 = Array(3, 3)
for i in range(3):
    for j in range(3):
        a1.SetValue(i, j,i+j)
a1.PrintValue()


# In[56]:


#Subtraction
a3 = a1.SubValues(a1,a2)


# In[63]:


#Multiplication
a4 = a1.MultValues(a1,a2)


# # Q2

# In[33]:


import numpy as np
array1 = np.array([[1,2,3,4],[5,6,7,8]], dtype=np.int64)
print(array1)


# In[36]:


x = np.ones((3,4),dtype=np.int64)
print(x)


# In[39]:


y = np.zeros((2,3,4),dtype=np.int16)
print(y)


# In[40]:


array2 = np.random.random((2,2))
print(array2)


# In[41]:


array3 = np.full((3,3),7)
print(array3)


# In[42]:


array4 = np.identity(3,dtype=np.int64)
print(array4)


# In[43]:


add = np.add(x,y)
print(add)


# In[44]:


diff = np.subtract(x,y)
print(diff)


# In[45]:


mult = np.multiply(x,y)
print(mult)


# In[46]:


div = np.divide(y,x)
print(div)


# In[47]:


rem = np.remainder(y,x)
print(rem)


# In[48]:


result = np.array_equal(x,y)
print(result)


# In[ ]:




