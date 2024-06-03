class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0 for i in range(n)]
        count = [1 for i in range(n)]
        ans = 0
        for i in range(n):
            temp = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if temp < dp[j]:
                        temp = dp[j]
                        count[i] = count[j]
                    elif dp[j] == temp:
                        count[i] += count[j]
            dp[i] = temp + 1
            if dp[i] > dp[ans]:
                ans = i
        sol = 0
        for i in range(n):
            if dp[i] == dp[ans]:
                sol += count[i]
        return sol