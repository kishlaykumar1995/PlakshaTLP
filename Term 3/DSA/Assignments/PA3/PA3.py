# %%
class HashTableChain:
    def __init__(self, size=10000, file=None):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        with open(file,'r') as f:
          for line in f.readlines():
            word = line.split('\n')[0]
            self.insert(word, 1)
        self.print_contents()

    
    # hash function to determine the index for a given key
    def hash_function(self, key):
      hash = 0
      n = len(key) # s is the given word
      for i in range(n):
        hash += self.g * hash + ord(key[i])     # g is the positive constant chosen by you
      index = hash % self.size     # capacity is total memory size allocated for hash table
      return index
    
    # insert a key-value pair to the hash table
    def insert(self, key, value):
      index = self.hash_function(key)
      if not self.table[index]:
        self.table[index] = []
        self.table[index].append([key, value])
        return
      for ele in self.table[index]:
        if ele[0] == key:
          ele[1]+=value
          return
      self.table[index].append([key, value])
      

    # retrieve the value for a given key
    def search(self, key):
      index = self.hash_function(key)
      if not self.table[index]:
        return None               # Or should we return -1?
      for ele in self.table[index]:
        if ele[0] == key:
          return ele
    
    def delete(self, key):
      index = self.hash_function(key)
      if not self.table[index]:
        return None
      for ele in self.table[index]:
        if ele[0] == key:
          self.table[index].remove(ele)
    
    def print_contents(self):
      # Print the contents of the hash table to a file
      with open("Chaining.txt", "w") as f:
        for chain in self.table:
          if chain is not None:
            for word, count in chain:
              f.write(f"{word} {count}\n")



# %%
class HashTableLinProb:
    def __init__(self, size=60000, file=None):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        with open(file,'r') as f:
          for line in f.readlines():
            word = line.split('\n')[0]
            self.insert(word, 1)
        self.print_contents()
    
    # hash function to determine the index for a given key
    def hash_function(self, key):
      hash = 0
      n = len(key) # s is the given word
      for i in range(n):
        hash += self.g * hash + ord(key[i])     # g is the positive constant chosen by you
      index = hash % self.size     # capacity is total memory size allocated for hash table
      return index
    
    # insert a key-value pair to the hash table
    def insert(self, key, value):
      index = self.hash_function(key)
      count = 0
      while True:
        if not self.table[index]:
          self.table[index] = [key, value]
          return
        if self.table[index][0] == key:
          self.table[index][1]+=value
          return
        index = (index+1)%self.size
        if count == self.size:
          return
        count+=1

    # retrieve the value for a given key
    def search(self, key):
      index = self.hash_function(key)
      count = 0
      while True:
        if self.table[index][0] == key:
          return self.table[index]
        index = (index+1)%self.size
        if count == self.size:
          return
        count+=1
    
    def delete(self, key):
      index = self.hash_function(key)
      count = 0
      while True:
        if self.table[index][0] == key:
          self.table[index] = None
          return
        index = (index+1)%self.size
        if count == self.size:
          return
        count+=1
    
    def print_contents(self):
      # Print the contents of the hash table to a file
      with open("Probing.txt", "w") as f:
        for ele in self.table:
          if ele:
            word,count = ele
            f.write(f"{word} {count}\n")





# %%
class HashTableChainDouble:
    def __init__(self, size=10000, file=None):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        with open(file,'r') as f:
          for line in f.readlines():
            word = line.split('\n')[0]
            self.insert(word, 1)
        self.print_contents()
    
    # hash function to determine the index for a given key
    def hash_function(self, key):
        hash = 0
        n = len(key) # s is the given word
        for i in range(n):
            hash += self.g * hash + ord(key[i])     # g is the positive constant chosen by you
        index = hash % self.size     # capacity is total memory size allocated for hash table
        return index

    def secondary_hash_function(self, key):
        hash = 0
        n = len(key)
        for i in range(n-1, -1, -1):                        # Use reverse order for secondary hash function
            hash += self.g**2 * hash + ord(key[i])**2     
        index = hash % self.size     
        return index
    
    # insert a key-value pair to the hash table
    def insert(self, key, value):
        index = (self.secondary_hash_function(key) + self.hash_function(key))%self.size
        if not self.table[index]:
            self.table[index] = []
            self.table[index].append([key, value])
            return
        for ele in self.table[index]:
            if ele[0] == key:
                ele[1]+=value
                return
        self.table[index].append([key, value])
    
    # retrieve the value for a given key
    def search(self, key):
        index = (self.secondary_hash_function(key) + self.hash_function(key))%self.size
        if not self.table[index]:
            return None               # Or should we return -1?
        for ele in self.table[index]:
            if ele[0] == key:
                return ele
    
    def delete(self, key):
        index = (self.secondary_hash_function(key) + self.hash_function(key))%self.size
        if not self.table[index]:
            return None
        for ele in self.table[index]:
            if ele[0] == key:
                self.table[index].remove(ele)
    
    def print_contents(self):
      # Print the contents of the hash table to a file
      with open("DoubleHashing.txt", "w") as f:
        for chain in self.table:
          if chain is not None:
            for word, count in chain:
              f.write(f"{word} {count}\n")


