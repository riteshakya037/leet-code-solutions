class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** (1 / 2))
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            elif total > c:
                right -= 1
            else:
                left += 1
        return False
