class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[0], i + 1, 0))

        return result
