class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = [[i + 1] for i in range(n)]
        ans = []
        tmp_k = k
        while k > 1:
            k -= 1
            for i in tmp:
                for j in range(i[-1] + 1, n + 1):
                    if n - j + 1 >= k:
                        ans.append(i + [j])
            tmp = ans
            ans = []
        return tmp
