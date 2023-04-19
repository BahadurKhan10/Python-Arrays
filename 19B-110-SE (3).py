#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Matrix: 
    def __init__(self,row,col): 
        self.row = row 
        self.col = col 
        self.data = [0 for i in range(row*col)] 

    def Location(self,i,j): 
        l = i * self.col + j 
        return l 
     

    def SetValue(self,i,j,v): 
        l = self.Location(i,j) 
        self.data[l] = v 

    def GetValue(self,i,j): 
        l = self.Location(i,j) 
        return self.data[l] 

    def Print(self): 
        for i in range(self.row): 
            for j in range(self.col): 
                print(self.GetValue(i,j), end = " ") 
            print('\n') 


    def printSecondaryDiagonal(mat, n):
        print("Secondary Diagonal: ", end = "")
 
        for i in range(n):
            for j in range(n):
 
            # Condition for secondary diagonal
                if ((i + j) == (n - 1)):
                    print(mat[i][j], end = ", ")
        print()
 


# In[44]:


#Driver Code
row = 3 
col = 3 
obj = Matrix(row,col) 
for i in range(row): 
    for j in range(col): 
        obj.SetValue(i,j,i+j) 

obj.Print() 
n = 4
a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ]]

printSecondaryDiagonal(a, n)

