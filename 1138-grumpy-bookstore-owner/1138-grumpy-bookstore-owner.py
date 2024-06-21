class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0

        # Calculate the total satisfaction without using the grumpy window
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        # Calculate the initial window of size X
        max_window_sum = 0
        current_window_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_window_sum += customers[i]

        max_window_sum = current_window_sum

        # Slide the window across the array
        start = 1
        end = minutes

        while end < len(customers):
            if grumpy[start - 1] == 1:
                current_window_sum -= customers[start - 1]
            if grumpy[end] == 1:
                current_window_sum += customers[end]

            max_window_sum = max(max_window_sum, current_window_sum)
            start += 1
            end += 1

        return total_satisfied + max_window_sum