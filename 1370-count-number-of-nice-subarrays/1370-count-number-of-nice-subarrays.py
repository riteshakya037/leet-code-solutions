class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        n = 0
        c = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                n += 1
                c = 0
            while n == k:
                c += 1
                if nums[l] % 2:
                    n -= 1
                l += 1
            res += c
        return res
