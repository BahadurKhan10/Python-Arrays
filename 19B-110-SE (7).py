#!/usr/bin/env python
# coding: utf-8

# In[39]:


from collections import defaultdict 
class Shareddata: 
    def __init__(self): 
        self.Value=5 
        A= "Nust Islamabad"
        B="UIT Karachi"
        C="UET Lahore" 
        D="BZU Multan" 
        E="Faislabad Uni" 
        self.V_org=[a,b,c,d,e] 
        self.graph=None 
        
    def build_graph(): 
        edges = [ 
            ["A", "B"],["B", "C"], 
            ["C", "D"],["A", "D"],
            ["C", "E"],["E", "D"] 
        ] 
        graph = defaultdict(list) 
        for edge in edges: 
            a, b = edge[0], edge[1] 
          
        # Creating the graph  
        # as adjacency list 
            graph[a].append(b) 
            graph[b].append(a) 
        return graph 
    
    def calculate_cost(graph, start, goal): 
        explored = [] 
        queue = [[start]] 

# If the desired node is reached 
        if start == goal: 
            print("Same Node") 
            return
          
#Loop to traverse the graph  
 
        while queue: 
            path = queue.pop(0) 
            node = path[-1] 
          
 #check if the current node is not visited 
            if node not in explored: 
                neighbours = graph[node] 
              
            # Loop to iterate over the  
            # neighbours of the node 
                for nod in neighbours: 
                    new_path = list(path) 
                    new_path.append(nod) 
                    queue.append(new_path) 
                  
                # ##Condition to check if the  
                # neighbour node is the goal 
                    if nod == goal: 
                        print("Shortest path = ", *new_path) 
                        return
                explored.append(node) 
  
    # Condition when the nodes are not connected 
        print("So sorry, but a path conncting path doesn't exist") 
        return


# In[40]:


gaph = {'Nust Islamabad': ['UIT Karachi', 'BZU Multan'], 
            'UIT Karachi': ['Nust Islamabad', 'UET Lahore'], 
            'UET Lahore': ["UIT Karachi",'BZU Multan',"Faislabad Uni"], 
            'BZU Multan': ['UET Lahore', 'Nust Islamabad',"Faislabad Uni"], 
            'E': ['UET Lahore', 'BZU Multan']} 
      
gg=Shareddata
gg.build_graph()
gg.calculate_cost(gaph,'Nust Islamabad','UIT Karachi')

