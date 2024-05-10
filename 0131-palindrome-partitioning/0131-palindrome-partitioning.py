class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                item = s[i : j + 1]
                if self.isPali(item):
                    part.append(item)
                    dfs(j + 1)
                    part.pop()

        dfs(0)

        return res

    def isPali(self, s: str):
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l - 1 - i]:
                return False
        return True
