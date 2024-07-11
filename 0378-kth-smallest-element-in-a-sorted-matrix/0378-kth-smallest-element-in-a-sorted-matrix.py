class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat = []
        for row in matrix:
            mat.extend(row)

        mat.sort()
        return mat[k - 1]
