class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        # Iterate over all possible combinations of numbers using bitmask
        for bitmask in range(1, 1 << 9):
            curr = []
            total_sum = 0
            
            for i in range(1, 10):
                if bitmask & (1 << (i - 1)):  # Check if ith bit is set
                    curr.append(i)
                    total_sum += i
            
            if len(curr) == k and total_sum == n:
                res.append(curr)
        
        return res