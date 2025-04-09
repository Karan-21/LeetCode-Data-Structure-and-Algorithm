class Node:

    def __init__(self,key,val):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def removeLeft(self,node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insertRight(self,node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeLeft(self.cache[key])
            self.insertRight(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeLeft(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insertRight(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.removeLeft(lru)
            del self.cache[lru.key]    
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
