class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            left, right = 0, c
            while left <= right:
                mid = (left + right) // 2
                if i * i + mid * mid == c:
                    return True
                if i * i + mid * mid > c:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
