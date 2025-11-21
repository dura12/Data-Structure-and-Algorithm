class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        q = []
        for key , value in dic.items():
            if len(q) == k:
                if q[0][0] < value :
                    heappop(q)
                    heappush(q , (value ,key))
            else:
                heappush(q , (value ,key))
        return [value for key , value in q]