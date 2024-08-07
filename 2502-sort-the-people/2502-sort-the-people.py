class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        d = dict(zip(heights, names))
        h = sorted(heights, reverse=True)
        return [d[height] for height in h]
