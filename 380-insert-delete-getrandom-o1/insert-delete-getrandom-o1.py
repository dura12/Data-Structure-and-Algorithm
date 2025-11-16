import random
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.lst = []


    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.lst)
        self.lst.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        last_value = self.lst[-1]
        self.lst[index] = last_value
        self.lst.pop()
        self.hashmap[last_value] = index
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()