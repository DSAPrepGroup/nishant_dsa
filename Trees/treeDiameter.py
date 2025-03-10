class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        height(root)
        return self.max_diameter

#Brute Force Solution
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_height(root):
            if not root:
                return 0
            
            left_height = max_height(root.left) + 1
            right_height = max_height(root.right) + 1

            ans = max(left_height, right_height)

            return ans
        
        def treeDiameter(root):
            if not root:
                return 0

            left_diameter = self.max_height(root.left)
            right_diameter = self.max_height(root.right)

            diameter = left_diameter + right_diameter

            sub = max(self.treeDiameter(root.left), self.treeDiameter(root.right))

            return max(diameter, sub)

