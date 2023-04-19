#!/usr/bin/env python
# coding: utf-8
Q1
# In[40]:


def BrainSearch(array, e,left_index,right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index)//2
    if mid_index >= len(array) or mid_index <0:
        return -1
    
    mid_num= array[mid_index]
    
    if mid_num == e:
        return mid_index
    
    if mid_num < e:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
        
    return BrainSearch(array,e,left_index, right_index)

array=[-1,2,3,5,4,97,7,44,22]
e=0
i =BrainSearch(array,e,0,len(array))
print(i)

Q2
# In[21]:


def RotateRight(array, n): 
    temp = array[0] 
    for i in range(n-1): 
        array[i] = array[i + 1] 
    array[n-1] = temp 
          

def printArray(array, size): 
    for i in range(size): 
        print ("% d"% array[i], end =" ") 
  
   
# Driver program to test above functions 
array = [1, 2, 3, 4, 5] 
RotateRight(array, 2) 
printArray(array, 5) 

Q3
# In[53]:


class DoubleStack: 
    def __init__(self, n):
        self.size = n 
        self.arr = [None] * n 
        self.top1 = -1 
        self.top2 = self.size
        
    def push1(self, x): 
        if self.top1 < self.top2 - 1 : 
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else: 
            print("Stack Overflow ") 
            exit(1) 

    def push2(self, x): 
        #For stack 2
        if self.top1 < self.top2 - 1: 
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x 

        else : 
            print("Stack Overflow ") 
            exit(1) 

            
    def pop1(self): 
        if self.top1 >= 0: 
            x = self.arr[self.top1] 
            self.top1 = self.top1 -1
            return x 
        else: 
            print("Stack Underflow ") 
            exit(1)
            
    def pop2(self): 
        if self.top2 < self.size: 
            x = self.arr[self.top2] 
            self.top2 = self.top2 + 1
            return x 
        else: 
            print("Stack Underflow ") 
            exit() 
            
ts =DoubleStack(5) 
ts.push1(5)
ts.push1(6)
ts.push1(10)
ts.push1(16)
ts.push2(13) 
ts.push2(19)
ts.push2(42) 
ts.push2(88)
print("Popped element from stack1 is " + str(ts.pop1()))
print("Popped element from stack2 is " + str(ts.pop2())) 

Q4
# In[68]:


class Deque:
    def __init__(self, limit = 10):
        self.array = []
        self.limit = limit

    def isEmpty(self):
        return len(self.array) <= 0

    def isFull(self):
        return(len(self.array)>=self.limit)

    def InsertFront(self, data):
        if self.isFull():
            return "Overflow Error"
        else:
            self.array.append(data)

    def GetFront(self):
        print(self.array[0])

    def DeleteFront(self):
        if self.isFull():
            return "Overflow Error"
        else:
            return self.array.pop()
        
    def size(self):
        return len(self.array)

x = Deque()
x.InsertFront(81)
x.InsertFront(42)
x.InsertFront(10)
x.GetFront()

Q5
# In[27]:


# Node class 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def deleteNode(self, key): 
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return

        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next

# if key was not present in 
        if(temp == None): 
            return

# Unlink the node from linked list 
        prev.next = temp.next
        temp = None

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data , end = ' ') 
            temp = temp.next

    def removeDuplicates(self): 
        temp = self.head 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data: 
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else: 
                temp = temp.next
        return self.head 

# Driver Code 
llist = LinkedList() 

llist.push(20) 
llist.push(13) 
llist.push(13) 
llist.push(11) 
llist.push(11) 
llist.push(11) 
print ("Created Linked List: ") 
llist.printList() 
print() 
print("Linked List after removing duplicate elements:") 
llist.removeDuplicates() 
llist.printList() 

