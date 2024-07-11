class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Set the range of the search to be between the smallest element
        # and the largest element in the matrix
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        
        # Binary search for the kth smallest element
        while left < right:
            mid = left + (right - left) // 2
            print("mid:", mid)
            cnt = 0
            j = n - 1
            # Count the number of elements in the matrix 
            # that are less than or equal to mid
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                cnt += j + 1
            print("cnt:", cnt)
            # Update the range of the search
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        
        return left
