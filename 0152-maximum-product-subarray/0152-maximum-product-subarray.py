class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            tempMax = curMax * n
            tempMin = curMin * n
            curMax = max(tempMax, tempMin, n)
            curMin = min(tempMax, tempMin, n)
            res = max(curMax, res)

        return res
