class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        R = len(matrix)
        C = len(matrix[0])
        numIdxMap = {}
        result = []

        for i in range(R):
            row = matrix[i]
            minColIdx = row.index(min(matrix[i]))
            minValInRow = matrix[i][minColIdx]
            isLuckyNum = True

            for r in range(R):
                if r != i and matrix[r][minColIdx] > minValInRow:
                    isLuckyNum = False
                    break

            if isLuckyNum:
                result.append(minValInRow)

        return result
