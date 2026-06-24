# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def morris(root,k):
           
            current = root

            while current:
                if current.left is None:
                    k -= 1
                    if k == 0:
                        return current.val
                    current = current.right
                else:
                    predecessor = current.left

                    while predecessor.right and predecessor.right is not current:
                        predecessor = predecessor.right
                    
                    if predecessor.right is None:
                        predecessor.right = current
                        current  = current.left
                    else:
                        predecessor.right = None
                        k -= 1
                        if k == 0:
                            return current.val
                        current = current.right
            return  -1
        return morris(root,k)