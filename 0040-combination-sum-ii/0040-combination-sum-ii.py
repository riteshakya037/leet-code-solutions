class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for _ in range(target + 1)]

        dp[0].add(())

        for num in candidates:
            for t in range(target, num - 1, -1):
                for prev_comb in dp[t - num]:
                    dp[t].add(prev_comb + (num,))

        return list(dp[target])
