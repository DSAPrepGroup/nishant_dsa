"""
Swap the children and recursively keep on doing it Depth First Search

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque(root)

        while queue:
            node = queue.popleft()
            node.left = node.right
            node.right = node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root