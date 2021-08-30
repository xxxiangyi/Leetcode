"""
Tree, Binary Search Tree

Time Complexity: O(logN) in the average, O(n) in the worst
Space Complexity: O(1)
"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root