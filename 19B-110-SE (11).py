#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[42]:


def WordSpell(file, spell):
    result = []
    x=open(file)
    content=x.readlines()

    
    for Word in content:
        if Word.startswith(spell.lower()) or Word.startswith(spell.upper()):
            result.append(Word.strip('\n'))
                
    return result
    
    

#Driver Code
spell = "pre"
file = "Words.txt"
print(WordSpell(file, spell))


# # Question 2

# In[121]:


class Node(object):
    def __init__(self, data):
        self.data = data #data
        self.next = None #pointer

class JukeNode(Node):
    def __init__(self, title, artist):
        data = [title, artist]
        self.title = title
        self.artist = artist
        self.times_played = 0
        Node.__init__(self, data)


    
class MySongs(LinkedList):
    def __init__(self):
        self.head = None
        
    
    def insert(self, new_node):
        end_node=self.head
    #1st condition; if list is empty
        if self.head==None:
            self.head = new_node
        
    #2nd condition; if list is not empty
        else:
            end_node = self.head
            while end_node.next !=None:
                    end_node = end_node.next
            end_node.next=new_node

            

    def delete(self, title):
        current_node = self.head
        previous_node = None
        condition = False
        
        while current_node and condition is False:
            if current_node.title != title:
                previous_node = current_node
                current_node = current_node.next
            else: 
                condition = True
        #1st condition:         
        if previous_node is None:
            self.head = current_node.next
        
        #2nd condition:
        elif current_node is None:
            return ("Data not in list")
        
        #3rd condition:
        elif current_node is not None and previous_node is not None:
            previous_node.next = current_node.next
        return True
    
    def display(self, status=True):
        i = self.head
        data = []
        while i != None: #Reaching toward the end node
            if status == True:
                print("-playing " + i.title + "-")
            data.append([i.title, i.artist])
            i= i.next
        return data
    
    def search(self, title):
        current_node = self.head
        found = False
        while current_node != None:
            if current_node.data[0] == title: #if song is found
                found = True
                break
            current_node = current_node.next #moving to next node
        return found
    
    def update_times_played(self, title):
        current_node = self.head
        favSong_status = False
        
        while current_node != None: #reaching toward end node
            if current_node.data[0] == title:
                current_node.times_played += 1
                #If song is played 3 times
                if current_node.times_played == 3:
                    favSong_status = True
            current_node = current_node.next  # moving to the next node / continous process in while loop 
        return favSong_status
    
    def getSongDetails(self, title):
        current_node = self.head
        data = []
        while current_node != None: #Reaching to the end node
            if current_node.data[0] == title:
                data = current_node.data
                break
            current_node = current_node.next #moving to next node
        return data

class MyFavorites(LinkedList):
    def __init__(self):
        self.head = None
        
    
    def insert(self, new_node):
        end_node=self.head
    #1st condition; if list is empty
        if self.head==None:
            self.head = new_node
        
    #2nd condition; if list is not empty
        else:
            end_node = self.head
            while end_node.next !=None:
                    end_node = end_node.next
            end_node.next=new_node

            

    def delete(self, title):
        current_node = self.head
        previous_node = None
        condition = False
        
        while current_node and condition is False:
            if current_node.title != title:
                previous_node = current_node
                current_node = current_node.next
            else: 
                condition = True
        #1st condition:         
        if previous_node is None:
            self.head = current_node.next
        
        #2nd condition:
        elif current_node is None:
            return ("Data not in list")
        
        #3rd condition:
        elif current_node is not None and previous_node is not None:
            previous_node.next = current_node.next
        return True
    
    def display(self, status=True):
        i = self.head
        data = []
        while i != None: #Reaching toward the end node
            if status == True:
                print("-playing " + i.title + "-")
            data.append([i.title, i.artist])
            i= i.next
        return data
    
    def search(self, title):
        current_node = self.head
        found = False
        while current_node != None:
            if current_node.data[0] == title: #if song is found
                found = True
                break
            current_node = current_node.next #moving to next node
        return found
    
    def update_times_played(self, title):
        current_node = self.head
        favSong_status = False
        
        while current_node != None: #reaching toward end node
            if current_node.data[0] == title:
                current_node.times_played += 1
                #If song is played 3 times
                if current_node.times_played == 3:
                    favSong_status = True
            current_node = current_node.next  # moving to the next node / continous process in while loop 
        return favSong_status
    
    def getSongDetails(self, title):
        current_node = self.head
        data = []
        while current_node != None: #Reaching to the end node
            if current_node.data[0] == title:
                data = current_node.data
                break
            current_node = current_node.next #moving to next node
        return data

class MyJukeBox:
    def __init__(self):
        self.playlist = MySongs()
        self.favorites = MyFavorites()
    
    def InsertSong(self, title, artist):
        newNode = JukeNode(title, artist)
        self.playlist.insert(newNode)
    
    def PlayList(self):
        self.playlist.display()

    def PlayFav(self):
        return self.favorites

    
    def PlaySong(self, title):
        song_status = self.playlist.search(title)
        if song_status == True:
            print("-playing " + title + "-")
            update_favorites = self.playlist.update_times_played(title)
            if update_favorites == True:
                data = self.playlist.getSongDetails(title)
                self.AddtoFav(data[0], data[1])
        else:
            print("Song does not exist!")
            
    
    def AddtoFav(self, title, artist):
        self.favorites.insert(JukeNode(title, artist))
        print(title + " has been added to favorites")
        
    def GetFav(self):
        list_songname= []
        data = self.favorites.display(False)
        for song in data:
            list_songname.append(song[0])
            return list_songname

    
    def DeleteSong(self, title):
        delete_from_list1 = self.playlist.delete(title)
        delete_from_list2 = self.favorites.delete(title)
        if delete_from_list1 == True and delete_from_list2 == True:
            print(title + " has been deleted")
        if delete_from_list1 == True:
            print(title + " has been deleted from the list")
            
    def Sort(self):
        x=self.playlist
        return x
    

#Driver Code
Obj = MyJukeBox()
Obj.InsertSong("Radioactive", "Imagine Dragons")
Obj.InsertSong("Girls Like you", "Maroon5")
Obj.InsertSong("Demons", "Imagine Dragons")
Obj.PlaySong("Demons")
Obj.PlaySong("Girls Like you")
Obj.PlaySong("Girls Like you")
Obj.PlaySong("Girls Like you")
Obj.Sort()
print(Obj.GetFav())
Obj.DeleteSong("Radioactive")


# # Question 3

# In[120]:


#Question 3    
from queue import Queue

class BankQueue:
    q1 = Queue(maxsize=10) #allowing 10 people per queue
    q2 = Queue(maxsize=10)
    q3 = Queue(maxsize=10)
    q4 = Queue(maxsize=10)

    def __init__(self, typeID, size):
        self.type = typeID
        self.size = size

    def EnqueueCustomer(self, time):
        try:
            if self.type == '1':
                self.q1.put(time)
            if self.type == '2':
                self.q2.put(time)
            if self.type == '3':
                self.q3.put(time)
            else:
                self.q4.put(time)
        except:
            pass
        
    def DequeueCustomer(self):
        try:
            if self.type == '1':
                return self.q1.get()
            if self.type == '2':
                return self.q2.get()
            if self.type == '3':
                return self.q3.get()
            else:
                return self.q4.get()
        except:
            pass
        
    def IsFull(self):
        try:
            if self.type == '1':
                return self.q1.full()
            if self.type == '2':
                return self.q2.full()
            if self.type == '3':
                return self.q3.full()
            else:
                return self.q4.full()
        except:
            pass
        
    def IsEmpty(self):
        try:
            if self.type == '1':
                return self.q1.empty()
            if self.type == '2':
                return self.q2.empty()
            if self.type == '3':
                return self.q3.empty()
            else:
                return self.q4.empty()
        except:
            pass
        
    def QSize(self):
        try:
            if self.type == '1':
                return self.q1.qsize()
            if self.type == '2':
                return self.q2.qsize()
            if self.type == '3':
                return self.q3.qsize()
            else:
                return self.q4.qsize()
        except:
            pass
        
    def Summ(self):
        count =0
        for res in range(0,10):
            try:
                if self.type == '1':
                    count+=self.q1[i]
                    return count
                elif self.type == '2':
                    count += self.q2[i]
                    return count
                elif self.type == '3':
                    count += self.q3[i]
                    return count
                else:
                    count += self.q4[i]
                    return count
            except:
                pass

class BankSimulation:
    que = []
    time_taken = []
    def _init_(self, filename):
        self.filename = filename

    def Process(self):
        file = open('file.txt', 'r')
        content = file.read().split()
        for i in range(0, len(content)):
            if i % 2 == 0:
                self.que.append(content[i])
            else:
                self.time_taken.append(content[i])
        for i in range(420):
            if BankQueue.IsFull():
                return "Queue is currenty Full"
        else:
            BankQueue.EnqueueCustomer()

    def CustomersServed(self):
        res = []
        for i in range(0,4):
            a.append(BankQueue.QSize())
            return res

    def AverageTime(self):
        res = []
        for i in range(0,4):
            a.append(BankQueue.Summ()/BankQueue.QSize())
            return a

    def MaxLength(self):
        res = []
        for i in range(4):
            a.append(BankQueue.QSize())
            return res
  
    def NotServed(self):
        res = []
        if BankQueue.IsFull():
            a.append(self.time_taken)
            return res


# # Question 4

# In[122]:


def SortEmpire(file):
    searched_result = [] 
    x = open(file)
    content=x.readlines()
    
    for i in range(2021): #till this year
        searched_result.append([])

    for emperor in content:
        emperor = emperor.strip()
        data = emperor.split(", ") #as emperor name and death is separated by commas
        searched_result[int(data[1])].append(emperor)


#Printing answers in 1 list
    result = []
    for i in searched_result:
        for x in i:
            if i:
                result.append(x)
                
        final_string = '\n'.join(result)
            
    print(final_string)

#Driver Code
SortEmpire("emperors.txt")

