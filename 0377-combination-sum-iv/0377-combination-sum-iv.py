class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def combinationSum(nums, target):
            if target == 0:
                return 1

            if target in dp:
                return dp[target]

            comb = 0
            for num in nums:
                if target >= num:
                    comb += combinationSum(nums, target - num)

            dp[target] = comb
            return dp[target]

        return combinationSum(nums, target)