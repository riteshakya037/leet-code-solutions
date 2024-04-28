class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if i & (1 << j)]
            if subset not in res:
                res.append(subset)

        return res

        return res