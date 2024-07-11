class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Set the range of the search to be between the smallest element
        # and the largest element in the matrix
        left, right = matrix[0][0], matrix[-1][-1]

        def less_k(mid):
            count = 0
            j = n - 1
            # Count the number of elements in the matrix
            # that are less than or equal to mid
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            return count

        # Binary search for the kth smallest element
        while left < right:
            mid = left + (right - left) // 2
            # Update the range of the search
            if less_k(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
