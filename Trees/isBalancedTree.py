class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # returns a list with boolean and height
        def height(root):
            if not root:
                return [True, 0]
            
            left = height(root.left)
            right = height(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <=1
            return [balanced, max(left[1], right[1])+1]

        return height(root)[0]