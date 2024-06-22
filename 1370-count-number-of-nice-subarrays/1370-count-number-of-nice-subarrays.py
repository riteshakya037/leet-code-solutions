class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        count = 0
        odds = 0

        while right < len(nums):
            if nums[right] % 2 != 0:
                odds += 1
                count = 0
            
            while odds == k:
                if nums[left] % 2 == 0:
                    count += 1
                
                if nums[left] % 2 != 0:
                    odds -= 1
                    count += 1
                
                left += 1
            
            ans += count

            right += 1
        return ans