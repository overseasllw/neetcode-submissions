# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_idx = {val: i for i, val in enumerate(inorder)}
        pre_it = iter(preorder)

        def build(l, r ) -> Optional[TreeNode]:
            if l > r:
                return None
            
            root = TreeNode(next(pre_it))
            mid = in_idx[root.val]

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0,len(inorder) -1)