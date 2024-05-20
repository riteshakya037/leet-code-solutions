class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        stringLen = len(s)

        for i in range(stringLen):
            # odd length
            l, r = i, i

            while l >= 0 and r < stringLen and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < stringLen and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res
