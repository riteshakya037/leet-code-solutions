class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        start = 0
        qsize = 0
        initial_gap = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                qsize += 1
                initial_gap = 0
            while qsize == k:
                initial_gap += 1
                if nums[start] % 2:
                    qsize -= 1
                start += 1
            subarrays += initial_gap
        return subarrays
