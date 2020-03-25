"""
LeetCode 101. Symmetric Tree

Given a binary tree, check if it is a mirror of itself.
"""

class TreeNode():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isLeaf(self, treeNode):
        """
        Check if current treenode is a leaf
        """
        if not treeNode:
            return False

        if treeNode.left == None and treeNode.right == None:
            return True
        else:
            return False

    def check(self, leftTree, rightTree):
        """
        type leftTree: TreeNode
        type rightTree: TreeNode
        rtype: bool
        """
        if not leftTree and not rightTree:
            return True
        elif not leftTree or not rightTree:
            return False

        if leftTree.val != rightTree.val:
            return False

        return (self.check(leftTree.left, rightTree.right) and
                self.check(leftTree.right, rightTree.left))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif self.isLeaf(root):
            return True
        else:
            return self.check(root.left, root.right)


def main():
    pass

if __name__ == '__main__':
    main()
