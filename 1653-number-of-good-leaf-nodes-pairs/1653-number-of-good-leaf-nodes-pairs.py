# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        total = 0

        def dfs(root):
            if not root.left and not root.right:
                return [1]

            descendants = []
            nonlocal total
            left = dfs(root.left) if root.left else []
            right = dfs(root.right) if root.right else []

            for i in left:
                if (
                    i >= distance
                ):  # if left tree leaf node is already > distance on its own, no point checking whether it can be paired with leaf node from right tree
                    continue
                for k in right:
                    if i + k <= distance:
                        total += 1

            return [i + 1 for i in left + right]

        dfs(root)
        return total
