class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        dp = [[] for _ in range(l + 1)]
        dp[0].append([])

        for j in range(1, l + 1):
            temp = []
            for i in range(j):
                if self.isPali(s, i, j - 1):
                    for former in dp[i]:
                        to_add = former + [s[i:j]]
                        temp.append(to_add)
            dp[j] += temp
        return dp[l]

    def isPali(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True
