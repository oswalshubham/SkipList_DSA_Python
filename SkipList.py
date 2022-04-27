import random


class OrderedDictionary:
    def insertElement(self, key, value):
        pass

    def removeElement(self, key):
        pass

    def findElement(self, key):
        pass

    def closestKeyAfter(self, key):
        pass

    def size(self) -> int:
        pass


class Node():
        def __init__(self,key,value,level):
            self.key=key
            self.value=value
            self.links=[None]*level

        def __str__(self):
            return "("+str(self.key)+","+str(self.value)+")" 
            

class SkipList(OrderedDictionary):
    def __init__(self):
        #total number of levels allowed
        self.MAX_Level = 10
        #The first or head node of Skiplist, will always be at the start of top level
        self.First = Node(None, None, self.MAX_Level)
        #total levels in SkipList
        self.Level = 0
        #total nodes in skiplist 
        self.Size = 0
        #probability of node height
        self.RProb = 0.3
        return

    def closestKeyBefore(self, key):
        Stack=[None]*self.Level
        node=self.First
        for i in range(self.Level- 1, -1, -1):
            while node.links[i] and node.links[i].key<key:
                node=node.links[i]   
            Stack[i] = node 

        return Stack,node

    def closestKeyAfter(self, key):
        Stack, node = self.closestKeyBefore(key)

        while node.links[0] and node.links[0].key <= key:
            node = node.links[0]

        return node.links[0].key if node.links[0] else None

    def findElement(self,key):

        node=self.First
        for level in range(self.Level - 1,-1,-1):
            #When searching in this level, if the key is greater than the key of the next node, move forward
            while node.links[level] and node.links[level].key<key:
                node=node.links[level]
             # if key is found, else move downwards level wise
            if node.links[level] and node.links[level].key == key:
                return node.links[level].value
        return None

    def insertElement(self,key,value):

        Stack, node= self.closestKeyBefore(key)
            
        #if node already exits in skipList, updating value of key
        if node.links[0] and node.links[0].key==key:
                node.links[0].value=value
                return None
                
        if Stack == None:
            #print("Node already exists. Value updated.")
            return

        #deciding level height for node to be inserted
        newLevel=self.random_height()
        newNode= Node(key,value,newLevel)
        for i in range(newLevel):
            if i<self.Level:
                newNode.links[i]=Stack[i].links[i]
                Stack[i].links[i]=newNode
            else:
                self.First.links[i]=newNode
        self.Size+=1
        self.Level=max(self.Level, newLevel)
        return None

    

    def removeElement(self,key):
        Stack=[None]*self.Level
        node=self.First
         # to check whether node is found, initially False
        flag = False
        for i in range(self.Level - 1, -1, -1):
            while node.links[i] and node.links[i].key<key:
                node=node.links[i]
            #node found in skipList
            if node.links[i] and node.links[i].key==key:
                flag=True
            Stack[i]=node

        #if node not present in skipList
        if not flag:
            print("Node not found.")
            return None
        #else if node is present
        # the node to be deleted
        delnode = node.links[0]

        #the number of links to this node will be less than or equal to stack
        #setting the links from delnode to corresponding stack element
        for i in range (len(delnode.links)): 
            Stack[i].links[i]=delnode.links[i]

        #updating size
        self.Size-=1
        
        #checking and updating number of levels, if top levels are empty, reduce number of levels
        newLevel=self.Level
        while newLevel>0 and not self.First.links[newLevel - 1]:
            newLevel-=1
        self.Level=newLevel

        return delnode.value

    #return total number of nodes in Linked List
    def size(self):
        return self.Size

     # generate a random number of layers for node
    def random_height(self):
        level=1
        while random.random()<self.RProb and level<self.MAX_Level:
            level+=1
        return level

    #display Skiplist level wise
    def display(self):
        print("")
        print("---Current SkipList---")
        result=""
        for i in range(self.Level - 1, -1, -1):
            result+= "Level "+str(i)+ ": head->"
            node = self.First
            while node.links[i]:
                result+=str(node.links[i])+"->"
                node=node.links[i]
            result+='tail\n'
        print("Total Levels in SkipList : "+str(self.Level))
        return result