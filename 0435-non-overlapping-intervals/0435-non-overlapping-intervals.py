class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        ans = 0
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < prevEnd:
                ans += 1
            else:
                prevEnd = intervals[i][1]
        return ans
