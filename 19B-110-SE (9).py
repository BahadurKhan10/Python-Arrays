#!/usr/bin/env python
# coding: utf-8

# DSA Assignment 1

# In[7]:


class SharpSearch:
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.last = None

    def SearchFirst(self, n):
        cou = 0
        for i in self.data:
            if i == n:
                return cou
            cou += 1
        return -1

    def SearchLast(self, n):
        lst = []
        x=len(self.data)
        for i in range(x):
            if self.data[i]==n:
                lst.append(i)
        if len(lst) > 0:
            return lst[-1]
        else:
            return -1

    def Search(self, n):
        if self.last != n and self.last != None:
            self.count = 0
        x = self.count
        self.count += 1
        self.last = n
        lst = []
        for i in range(len(self.data)):
            if self.data[i] == n:
                lst.append(i)
        if len(lst) > 0:
            try:
                return lst[x]
            except:
                return -1
        else:
            return -1

    def SearchAll(self, n):
        x = []
        cou = 0
        for i in self.data:
            if i == n:
                x.append(cou)
            cou += 1
        return x

s = SharpSearch([1,3,0,4,2,8,8])
print("SearchFirst 0:",s.SearchFirst(0))
print("SearchLast 8:",s.SearchLast(8))
print("SearchLast 4:",s.SearchLast(4))
print("SearchLast 77:",s.SearchLast(77))
print("Search 4:",s.Search(4))
print("Search 4:",s.Search(4))
print("Search 4:",s.Search(4))
print("Search 4:",s.Search(4))
print("Search 8:",s.Search(8))
print("Search 8:",s.Search(8))
print("Search 88:",s.Search(88))
print("SearchAll 4:",s.SearchAll(4))


# In[ ]:




