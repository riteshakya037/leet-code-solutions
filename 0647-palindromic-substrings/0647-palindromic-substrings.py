class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            for a, b in zip(reversed(s[:i]), s[(i + 1):]):
                if a == b:
                    count += 1
                else:
                    break
            for a, b in zip(reversed(s[:(i + 1)]), s[(i + 1):]):
                if a == b:
                    count += 1
                else:
                    break
        return count
