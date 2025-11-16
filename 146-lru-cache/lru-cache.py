class Node:
    def __init__(self , key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head , self.tail = Node(0,0) , Node(0,0)
        self.head.next , self.tail.prev = self.tail , self.head
    def remove(self, node):
        prev , nxt = node.prev , node.next
        prev.next , nxt.prev = nxt , prev
        node.prev = None
        node.next = None
        
    def insert(self, node):
        prev, nxt= self.tail.prev , self.tail
        prev.next =nxt.prev =  node
        node.prev , node.next = prev , nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return 
        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node
        if self.capacity < len(self.cache):
            lcu = self.head.next
            key = lcu.key
            self.remove(lcu)
            del self.cache[key]
        
    

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)