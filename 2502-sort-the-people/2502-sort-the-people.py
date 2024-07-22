class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        descend = [""] * len(names)
        d = dict(zip(heights, names))

        h = sorted(heights)
        return [d[height] for height in h[::-1]]
