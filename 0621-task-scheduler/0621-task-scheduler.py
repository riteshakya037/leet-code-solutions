class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1]))

        maxFrequency = frequencies.popitem()[1]
        idleTimes = (maxFrequency - 1) * n

        while frequencies and idleTimes > 0:
            idleTimes -= min(maxFrequency - 1, frequencies.popitem()[1])
        idleTimes = max(0, idleTimes)

        return len(tasks) + idleTimes
