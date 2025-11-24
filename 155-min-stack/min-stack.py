class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
        self.prev = None
class MinStack:

    def __init__(self):
        self.stack = []
        self.head , self.tail = Node(0) , Node(0)
        self.head.next , self.tail.prev = self.tail , self.head
    def push(self, val: int) -> None:
        node = Node(val)
        self.insert(node)
        self.stack.append(node)
    def insert(self, node):
        prev , nxt = self.tail.prev  ,self.tail
        if prev.val > node.val:
            prev.next = self.tail.prev = node
            node.prev , node.next = prev , nxt
        else:
            prev , nxt = self.head ,   self.head.next
            prev.next = nxt.prev = node
            node.next , node.prev = nxt , prev
    def remove(self , node):
        prev , nxt = node.prev , node.next
        prev.next , nxt.prev = nxt , prev
    def pop(self) -> None:
        if not self.stack:
            return -1
        node = self.stack.pop()
        self.remove(node)
        return node.val

    def top(self) -> int:
        node = self.stack[-1]
        return node.val
        

    def getMin(self) -> int:
        return self.tail.prev.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()