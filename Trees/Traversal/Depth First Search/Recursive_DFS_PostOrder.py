def dfs(root):
    if not root:
        return 
    dfs(root.left)
    dfs(root.right)
    print(root.val, end=" ")
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create sample tree nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Link the nodes to form a binary tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# The tree looks like this:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

# Root of the tree is node1
root = node1

dfs(root)