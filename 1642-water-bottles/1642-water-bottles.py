class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def exchange(numBottles, numExchange):
            if numBottles < numExchange:
                return 0
            newBottles, r = divmod(numBottles, numExchange)
            return newBottles + exchange(newBottles + r, numExchange)

        return numBottles + exchange(numBottles, numExchange)
