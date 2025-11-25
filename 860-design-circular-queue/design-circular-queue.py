class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.cap = 0
        self.head , self.tail = Node(0) , Node(0)
        self.head.next , self.tail.prev = self.tail , self.head
        self.head.prev , self.tail.next = self.tail , self.head
    def insert(self , node):
        prev , nxt = self.tail.prev , self.tail
        prev.next =   nxt.prev = node
        node.next , node.prev = nxt , prev
        self.cap += 1
    def remove(self):
        node = self.head.next
        h , nxt = self.head , node.next
        h.next , nxt.prev = nxt , h
        node.next = None
        node.prev = None
        self.cap -= 1
    def enQueue(self, value: int) -> bool:
        if self.cap == self.capacity:
            return False
        new_node = Node(value)
        self.insert(new_node)
        return True
    def deQueue(self) -> bool:
        if self.cap == 0:
            return False
       
        self.remove()
        return True

    def Front(self) -> int:
        if self.cap == 0:
            return -1
        node =self.head.next
        return node.val
        

    def Rear(self) -> int:
        if self.cap == 0:
            return -1
        node =self.tail.prev
        return node.val
        

    def isEmpty(self) -> bool:
        return self.cap == 0
        

    def isFull(self) -> bool:
        return self.cap == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()