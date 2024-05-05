class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(pos, curr, target):
            if len(curr) == k:
                if target == 0:
                    res.append(curr[:])
                return

            for i in range(pos + 1, 10):
                if i <= target:
                    curr.append(i)
                    dfs(i, curr, target - i)
                    curr.pop()
                else:
                    return

        dfs(0, [], n)
        return res
