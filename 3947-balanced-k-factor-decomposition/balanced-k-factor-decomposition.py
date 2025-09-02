class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        self.ans = []
        self.min_diff = float('inf')
        if k == 1:
            return [n]
        
        self.ans = [1] * (k - 1) + [n]
        self.min_diff = n - 1
        def dfs(start_factor, current_product, count, path):
            if count == k:
                if current_product == n:
                    current_max = max(path)
                    current_min = min(path)
                    if current_max - current_min < self.min_diff:
                        self.min_diff = current_max - current_min
                        self.ans = list(path) 
                    if self.min_diff == 0:
                        raise StopIteration 
                return

            if current_product > n:
                return

            upper_bound = int((n // current_product)**0.5) + 1 
            if count == k - 1:
                if n % current_product == 0:
                    last_factor = n // current_product
                    if last_factor >= start_factor:
                        path.append(last_factor)
                        dfs(last_factor, n, k, path)
                        path.pop()
                return

            for factor in range(start_factor, upper_bound + 1):
                if current_product * factor > n:
                    break

                if (n % (current_product * factor)) == 0: 
                    path.append(factor)
                    dfs(factor, current_product * factor, count + 1, path)
                    path.pop()

        try:
            dfs(1, 1, 0, []) 
        except StopIteration:
            pass 
        return self.ans