class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_sum = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_sum += customers[i]

        satisfaction = total_sum
        start = 0
        end = start + minutes - 1

        while end < len(customers):
            temp_sum = 0
            for i in range(start, end + 1):
                if grumpy[i] == 1:
                    temp_sum += customers[i]

            satisfaction = max(satisfaction, total_sum + temp_sum)

            start += 1
            end += 1

        return satisfaction
