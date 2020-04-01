"""
A class for binary tree
"""
import math
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        # type x: integers
        self._value = x
        self._left = None
        self._right = None

    @property
    def value(self):
        if not self:
            return 'null'
        return self._value

    @property
    def left(self):
        # rtype: TreeNode
        if not self._left:
            return None
        return self._left

    @left.setter
    def left(self, tnode):
        self._left = tnode

    @property
    def right(self):
        # rtype: TreeNode
        if not self._right:
            return None
        return self._right

    @right.setter
    def right(self, tnode):
        self._right = tnode

    def is_leaf(self):
        if not self:
            return False

        if not self._left and not self._right:
            return True
        else:
            return False

    def print_node(self):
        val = 'null'
        leftVal = 'null'
        rightVal = 'null'

        if self:
            val = self._value
        else:
            val = 'null'

        if self._left:
            leftVal = self._left._value
        else:
            leftVal = 'null'

        if self._right:
            rightVal = self._right._value
        else:
            rightVal = 'null'

        print("value: {0}, left: {1}, right: {2}".
        format(val, leftVal, rightVal))

class Tree(object):
    def __init__(self):
        self._level = 0
        self._root = None # TreeNode

    @property
    def level(self):
        if not self._level:
            return None
        return self._level

    @level.setter
    def level(self, height):
        self._level = height

    @property
    def root(self):
        if not self._root:
            return None
        return self._root

    @root.setter
    def root(self, troot):
        self._root = troot

    def create(self, numbers):
        # Create a binary tree from a string of numbers
        # type numbers: a string array of numbers
        # rtype: TreeNode
        if not numbers:
            return None

        tree = list()

        # First node: it will be the root of the binary tree
        root = TreeNode(numbers[0])
        tree.append(root)

        # Loop over numbers
        level = 1
        count = 2 ** level # math.pow(2, level)
        parentIndex = 0 # Starting point to the parent nodes
        crIndex = 1
        while crIndex < len(numbers):
            for j in range(0, count):
                if (crIndex + j) < len(numbers):
                    if (numbers[crIndex + j] == 'null' or
                    numbers[crIndex + j] == 'Null'):
                        tree.append(None)
                    else:
                        tnode = TreeNode(numbers[crIndex + j])
                        pIndex = parentIndex + j / 2
                        tree.append(tnode)

                        # Connect to parent node
                        if j % 2 == 0:
                            tree[pIndex].left = tnode
                        else:
                            tree[pIndex].right = tnode

            # Update indexes
            crIndex += count
            parentIndex += 2 ** (level - 1)

            level += 1
            count = 2 ** level

        self._level = level
        self._root = root

        print(len(tree))
        for i in range(len(tree)):
            if not tree[i]:
                print('null')
            else:
                tree[i].print_node()

        return self._root

    def print_level_order(self):
        # Print a binary tree in level order, aka Breadth first search
        if not self._root:
            return None

        treeList = list()
        treeQueue = deque()
        treeQueue.append(self._root) # Add to the right side of the deque

        while(treeQueue):
            tNode = treeQueue.popleft() # Pop from the left side of the deque
            if tNode and not tNode.is_leaf():
                # Add tNode's left and right children to the deque
                if tNode.left:
                    # tNode.left is a TreeNode,
                    # tNode.left(), is trying to call a function name tNode.left()
                    treeQueue.append(tNode.left)
                else:
                    treeQueue.append(None)
                if tNode.right:
                    treeQueue.append(tNode.right)
                else:
                    treeQueue.append(None)

            if tNode:
                treeList.append(tNode.value)
            else:
                treeList.append('null')

        # Remove the last 'null' if existing
        listLen = len(treeList)
        while(treeList[listLen - 1] == 'null'):
            treeList.pop()
            listLen = len(treeList)

        print(treeList)

    def print_pre_order(self):
        # Print tree in pre-order (root, left, right)
        # aka Depth first search
        treeList = list()
        self.traverse_pre_order(self._root, treeList)

        print(treeList)

    def traverse_pre_order(self, tnode, tlist):
        # Base case: if is_leaf, add value and return
        if not tnode:
            return None

        tlist.append(tnode.value)
        self.traverse_pre_order(tnode.left, tlist)
        self.traverse_pre_order(tnode.right, tlist)

    def print_in_order(self):
        # Print tree in in-order (left, root, right)
        treeList = list()
        self.traverse_in_order(self._root, treeList)

        print(treeList)

    def traverse_in_order(self, tnode, tlist):
        if not tnode:
            return None

        if tnode.is_leaf():
            tlist.append(tnode.value)
            return None

        self.traverse_in_order(tnode.left, tlist)
        tlist.append(tnode.value)
        self.traverse_in_order(tnode.right, tlist)

    def print_post_order(self):
        # Print tree in post-order (left, right, root)
        treeList = list()
        self.traverse_post_order(self._root, treeList)

        print(treeList)

    def traverse_post_order(self, tnode, tlist):
        if not tnode:
            return None

        if tnode.is_leaf():
            tlist.append(tnode.value)
            return None

        self.traverse_post_order(tnode.left, tlist)
        self.traverse_post_order(tnode.right, tlist)
        tlist.append(tnode.value)

    def height(self):
        # Get tree height
        return self.cal_height(self._root)

    def cal_height(self, tnode):
        if not tnode:
            return 0

        return 1 + max(self.cal_height(tnode.left), self.cal_height(tnode.right))

    def is_symmetric(self):
        if not self._root:
            return True

        if self._root.is_leaf():
            return True
        else:
            return self.check_symmetric(self._root.left, self._root.right)

    def check_symmetric(self, leftTree, rightTree):
        if not leftTree and not rightTree:
            return True
        elif not leftTree or not rightTree:
            return False

        # Both left and right children exist
        if leftTree.value != rightTree.value:
            return False
        else:
            return (self.check_symmetric(leftTree.left, rightTree.right) and
                    self.check_symmetric(leftTree.right, rightTree.left))
