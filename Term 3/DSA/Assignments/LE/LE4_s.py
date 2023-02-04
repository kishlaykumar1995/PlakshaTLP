#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Lab Exercise - 4 
# Priority Queues

import sys

class PriorityQueue:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        # creating the list with indexing starting from 1 for simplicity
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
    
    def getParentIndex(self, index):
        return (index)// 2
    def leftchildIndex(self, index):
        return (2 * index) 
    def rightchildIndex(self, index):
        return (2*index)+1
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.leftchildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.rightchildIndex(index) < self.size
    def parent(self, index):
        return self.Heap[self.getParentIndex(index)]
    def leftchild(self, index):
        return self.Heap[self.leftchildIndex(index)]
    def rightchild(self, index):
        return self.Heap[self.rightchildIndex(index)]
    def isFull(self):
        return self.maxsize == self.size
    def swap(self, index1, index2):
        temp = self.Heap[index1]
        self.Heap[index1] = self.Heap[index2]
        self.Heap[index2] = temp
        
    # minHeapify method to minHeapify the node at pos
    def minHeapify(self, pos):
        if not self.hasLeftChild(pos):
            return

        smallest = self.leftchildIndex(pos)
        if self.hasRightChild(pos) and self.rightchild(pos) < self.leftchild(pos):
            smallest = self.rightchildIndex(pos)
        if self.Heap[pos] > self.Heap[smallest]:
            self.swap(pos, smallest)
            self.minHeapify(smallest)
        #pass
    
    def heapifyUp(self,index):
        
        if(self.hasParent(index) and (self.parent(index) > self.Heap[index])):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))
            
#     def heapifyDown(self, index):
#         self.minHeapify(index)

             
    # Write this function to insert a node into the heap

    def insert(self, element):
        if (self.isFull()):
            raise ('Heap is full')
        self.Heap[self.size+1] = element
        self.size += 1
        self.heapifyUp(self.size)
         # pass

    # Write this function to delete the rootNode
    def delete(self):
        if self.size == 0:
            raise ('Empty Heap')
        root_node = self.Heap[1]
        self.Heap[1] = self.Heap[self.size-1]
        self.size -= 1
        self.minHeapify(1)
        #return root_node
          #pass

    # Write this function to return the rootNode (here the minimum element in PQ)
    def minimumElement(self): 
        return self.Heap[1]
          #pass

    # Write this function to return the size of the PriorityQueue
    def sizeOfPq(self): 
        return self.size
          #pass

    # Write this function to return if the priorityQueue is empty or not
    # Return boolean value
    def isPqEmpty(self):
        return (self.sizeOfPq() == 0)
          #pass

    # Function to print the contents of the heap
    def printPriorityQueue(self):
          for i in range(1, (self.size//2)+1):
            print("Parent : "+ str(self.Heap[i])+" Left Child : "+
                      str(self.Heap[2 * i])+" Right Child : "+
                      str(self.Heap[2 * i + 1]))

    # Function to build the PriorityQueue using minHeap
    def priorityQueue(self): 
          for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)


# In[83]:


# # To verify your functions written above, run this code block

# if __name__ == "__main__":

#     # Creating a priorityQueue with maxsize = 40 using a MinHeap
#     pq = PriorityQueue(40)  
      
#     pq.insert(38)
#     pq.insert(65)
#     pq.insert(32)
#     pq.insert(88)
#     pq.insert(6)
#     pq.insert(24)
#     pq.insert(81)
#     pq.insert(99)
#     pq.insert(3)
#     pq.insert(79)
#     pq.insert(36)
#     pq.insert(57)
#     pq.insert(7)
#     pq.insert(50)
#     pq.insert(55)
#     pq.insert(70)
#     pq.insert(94)
#     pq.insert(28)
#     pq.insert(1)
#     pq.printPriorityQueue()
#     print()
#     print("The minimum element in the Priority Queue is : ", pq.minimumElement())
#     print()
#     print("The size of the Priority Queue is: ", pq.sizeOfPq())
#     print()
#     if pq.isPqEmpty(): 
#           print("The Priority Queue is empty")
#     else: 
#           print("The Priority Queue is not empty")
#     print()
#     print("Now, delete the root node of the Priority Queue.")
#     pq.delete()
#     print("After deleting, the minimum element in the Priority Queue is ", pq.minimumElement())
#     print()
#     pq.printPriorityQueue()


# In[ ]:




