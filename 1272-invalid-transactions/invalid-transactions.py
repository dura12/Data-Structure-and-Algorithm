class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = defaultdict(list)
        ans = []
        indexes = set()
        for i , transaction in enumerate(transactions):
            name , time , amount , city = transaction.split(",")
            if int(amount) > 1000:
                indexes.add(i)
            if name in dic:
                for values in (dic[name]):
                    prev_index, t , m , c  = values
                    if city != c and abs(int(time) - int(t)) <= 60:
                        indexes.add(prev_index)
                        indexes.add(i)
            dic[name].append([i,time,amount,city])
        for index in indexes:
            ans.append(transactions[index])
        return ans
        
        





                