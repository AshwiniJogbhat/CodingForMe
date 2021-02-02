# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trimSubTree(node):
            if not node: return node
            if node.val > high:
                return trimSubTree(node.left)
            elif node.val < low:
                return trimSubTree(node.right)
            else:
                node.left = trimSubTree(node.left)
                node.right = trimSubTree(node.right)
                return node
            
        return trimSubTree(root)
