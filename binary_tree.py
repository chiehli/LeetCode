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

    def is_equal(self, tnode):
        if not tnode or not self:
            return False

        if self._value == tnode.value:
            return True

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
    def __init__(self, numbers, tnode=None):
        if tnode:
            self._root = tnode # TreeNode
            self._height = tnode.height
        else:
            if numbers:
                self.create(numbers)

    @property
    def height(self):
        if not self._height:
            return None
        return self._height

    @height.setter
    def height(self, tHeight):
        self._height = tHeight

    @property
    def root(self):
        if not self._root:
            return None
        return self._root

    @root.setter
    def root(self, tRoot):
        self._root = tRoot

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

        self._height = level
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

    def get_height(self, tnode):
        # Get tree height
        return self.cal_height(tnode)

    def cal_height(self, tnode):
        if not tnode:
            return 0

        return 1 + max(self.cal_height(tnode.left), self.cal_height(tnode.right))

    def get_diameter(self, tnode):
        return self.cal_diameter(tnode)

    def cal_diameter(self, tnode):
        if not tnode:
            return 0

        diaRoot = self.get_height(tnode.left) + self.get_height(tnode.right)
        diaLeft = self.cal_diameter(tnode.left)
        diaRight = self.cal_diameter(tnode.right)
        return max(diaRoot, diaLeft, diaRight)

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

    def left_side_view(self):
        if not self._root:
            return None

        treeList = []
        max_level = []
        max_level.append(0)
        self.get_left_side(self._root, 1, max_level, treeList)

        print(treeList)

    def get_left_side(self, tnode, level, max_level, treeList):
        if not tnode:
            return None

        if level > max_level[0]:
            treeList.append(tnode.value)
            max_level[0] = level

        self.get_left_side(tnode.left, level + 1, max_level, treeList)
        self.get_left_side(tnode.right, level + 1, max_level, treeList)

    def right_side_view(self):
        if not self._root:
            return None

        treeList = []
        max_level = []
        max_level.append(0)
        self.get_right_side(self._root, 1, max_level, treeList)

        print(treeList)

    def get_right_side(self, tnode, level, max_level, treeList):
        if not tnode:
            return None

        if level > max_level[0]:
            treeList.append(tnode.value)
            max_level[0] = level

        self.get_right_side(tnode.right, level + 1, max_level, treeList)
        self.get_right_side(tnode.left, level + 1, max_level, treeList)

    def bottom_side_view(self):
        # bottom side view from left to right
        if not self._root:
            return None

        treeList = []
        self.get_bottom_side_view(self._root, treeList)

        print(treeList)

    def get_bottom_side_view(self, tnode, treeList):
        if not tnode:
            return None

        if tnode.is_leaf():
            treeList.append(tnode.value)

        self.get_bottom_side_view(tnode.left, treeList)
        self.get_bottom_side_view(tnode.right, treeList)

    def exist_path_sum(self, target_val):
        # A path sum is defined as the sum of node value from root to leave
        # This function finds if any path sum equals the input target_val
        if not self._root:
            return False

        return self.find_path_sum(self._root, target_val)

    def find_path_sum(self, tnode, target_sum):
        if not tnode:
            return False

        if tnode.is_leaf():
            if tnode.value == target_sum:
                return True

        target_sum -= tnode.value
        return (self.find_path_sum(tnode.left, target_sum) or
                self.find_path_sum(tnode.right, target_sum))

    def find_least_common_ancestor(self, tnode1, tnode2):
        # Given two tree nodes, find their least common ancestor in the binary treeNode
        # type tnode1, tnode2: TreeNode
        # rtype: TreeNode
        if (not self._root or not tnode1 or not tnode2 or
            not self.search(self._root, tnode1) or not self.search(self._root, tnode2)):
            return None

        return self.lca_helper(self._root, tnode1, tnode2)

    def lca_helper(self, root, tnode1, tnode2):
        if root.is_equal(tnode1) or root.is_equal(tnode2):
            return root

        tnode1_in_left = self.search(root.left, tnode1)
        tnode2_in_left = self.search(root.left, tnode2)

        if ((tnode1_in_left and not tnode2_in_left) or
            (not tnode1_in_left and tnode2_in_left)):
            # tnode1 and tnode2 are in different subtree, current root is the LCA
            return root
        elif tnode1_in_left and tnode2_in_left:
            return self.lca_helper(root.left, tnode1, tnode2)
        elif not tnode1_in_left and not tnode2_in_left:
            return self.lca_helper(root.right, tnode1, tnode2)

    def search(self, root, tnode):
        # Check if the tree node is in current binary tree
        # type tnode: TreeNode
        # rtype: bool
        if not root or not tnode:
            return False

        if root.is_equal(tnode):
            return True

        return self.search(root.left, tnode) or self.search(root.right, tnode)

    def find_tilt(self):
        """
        The tilt of a tree node is defined as the absolute difference between
        the sum of all left subtree node values and the sum of all right subtree
        node values. Null node has tilt 0.

        The tile of the whole tree is defined as the sum of all nodes' tilt.
        """
        if not self._root:
            return 0

        tilt_val = []
        tilt_val.append(0)
        self.tilt_helper(self._root, tilt_val)

        return tilt_val[0]

    def tilt_helper(self, root, tilt_val):
        if not root or root.is_leaf():
            tilt_val[0] += 0
            return 0

        left_sum = self.subtree_sum(root.left)
        right_sum = self.subtree_sum(root.right)
        tilt_val[0] += abs(left_sum - right_sum)

        return self.tilt_helper(root.left, tilt_val) + self.tilt_helper(root.right, tilt_val)

    def subtree_sum(self, tnode):
        if not tnode:
            return 0

        if tnode.is_leaf():
            return tnode.value

        return (tnode.value + self.subtree_sum(tnode.left) + self.subtree_sum(tnode.right))
