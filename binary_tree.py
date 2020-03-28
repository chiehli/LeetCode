"""
A class for binary tree
"""
import math

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
            return 'null'
        return self._left

    @left.setter
    def left(self, tnode):
        self._left = tnode

    @property
    def right(self):
        # rtype: TreeNode
        if not self._right:
            return 'null'
        return self._right

    @right.setter
    def right(self, tnode):
        self._right = tnode

    def print_node(self):
        val = 'null'
        leftVal = 'null'
        rightVal = 'null'

        if self:
            val = self._value

        if self._left:
            leftVal = self._left._value

        if self._right:
            rightVal = self._right._value

        print("value: {0}, left: {1}, right: {2}".
        format(val, leftVal, rightVal))

class Tree(object):
    def __init__(self):
        pass

    def create(self, numbers):
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

        print(len(tree))
        for i in range(len(tree)):
            if not tree[i]:
                print('null')
            else:
                tree[i].print_node()

        return root
