
class MagicDictionary:
    def __init__(self):
        self.dic = defaultdict(list)
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dic[len(word)] += [word]
    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.dic:
            return False
        for word in self.dic[len(searchWord)]:
            count = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    count += 1
                if count > 1:
                    break 
            if count == 1:
                return True
        return False

    
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)