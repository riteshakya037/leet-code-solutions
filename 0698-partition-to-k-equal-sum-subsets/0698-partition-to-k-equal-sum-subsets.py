class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        eSum, rem = divmod(sum(nums), k)
        nums.sort(reverse=True)
        if rem or nums[0] > eSum:
            return False

        def dfs(index, target, groups):
            if groups == k - 1:
                return True
            if index == n:
                return False

            num = nums[index]
            if num > target:
                return dfs(index + 1, target, groups)

            nums[index] = eSum + 1
            if num == target:
                return dfs(0, eSum, groups + 1)

            if dfs(index + 1, target - num, groups):
                return True

            nums[index] = num
            return dfs(index + 1, target, groups)

        return dfs(0, eSum, 0)
