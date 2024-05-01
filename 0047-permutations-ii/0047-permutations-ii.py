class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in count:
                if count[i] > 0:
                    perm.append(i)
                    count[i] -= 1

                    dfs()

                    count[i] += 1
                    perm.pop()

        dfs()
        return res