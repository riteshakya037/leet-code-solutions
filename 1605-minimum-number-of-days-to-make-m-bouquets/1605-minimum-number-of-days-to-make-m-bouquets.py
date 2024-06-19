class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isEnoughDays(days):
            flowers, bouquets = 0, 0
            for d in bloomDay:
                flowers = flowers + 1 if d <= days else 0
                if flowers == k:
                    bouquets += 1
                    if bouquets == m: break
                    flowers = 0
            
            return bouquets == m

        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if isEnoughDays(mid):
                right = mid
            else:
                left = mid + 1
        return left
