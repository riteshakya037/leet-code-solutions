class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total&1:
            return False 

        subSetsum = total >> 1 
        bitMask = 1
        for n in nums:
            bitMask = bitMask | bitMask << n 
        return bitMask & 1 << subSetsum
