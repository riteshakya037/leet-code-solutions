class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        target, rem = divmod(sum(nums), k)
        nums.sort(reverse=True)
        if rem or nums[0] > target:
            return False

        def dfs(index, total, groups):
            if groups == k - 1:
                return True
            if index == n:
                return False

            num = nums[index]
            if num > total:
                return dfs(index + 1, total, groups)

            nums[index] = target + 1
            if num == total:
                return dfs(0, target, groups + 1)

            if dfs(index + 1, total - num, groups):
                return True

            nums[index] = num
            return dfs(index + 1, total, groups)

        return dfs(0, target, 0)




