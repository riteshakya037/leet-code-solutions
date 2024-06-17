class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False

        l, r = 0, int(c**0.5)
        while l <= r:
            currSum = l**2 + r**2
            if currSum == c:
                return True
            elif currSum < c:
                l += 1
            else:
                r -= 1
        return False
