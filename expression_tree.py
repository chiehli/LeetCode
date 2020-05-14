"""
A class for binary tree
"""
import math
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        # type x: integer or string
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

class ExpressionTree(object):
    def __init__(self, expression, tnode=None):
        if tnode:
            self._root = tnode # TreeNode
            self._height = tnode.height
        else:
            if expression:
                self.create(expression)

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

    def create(self, strs):
        # Create an expression tree from a string of expression
        # type strs: a string array of expression
        # rtype: TreeNode
        if not strs:
            return None

        tree = list()

        # First node: it will be the root of the binary tree
        root = TreeNode(strs[0])
        tree.append(root)

        # Loop over numbers
        level = 1
        count = 2 ** level # math.pow(2, level)
        parentIndex = 0 # Starting point to the parent nodes
        crIndex = 1
        while crIndex < len(strs):
            for j in range(0, count):
                if (crIndex + j) < len(strs):
                    if (strs[crIndex + j] == 'null' or
                        strs[crIndex + j] == 'Null'):
                        tree.append(None)
                    else:
                        tnode = TreeNode(strs[crIndex + j])
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

    def evaluate(self, tnode):
        if not tnode:
            # note: should be None, raise exception
            raise Exception('Invalid tree input')

        if tnode.is_leaf():
            return tnode.value

        operator = tnode.value
        # to improve, map operation to function
        # call function in map instead of using multiple if-elses
        if tnode.left and tnode.right:
            if operator == '+':
                return (self.evaluate(tnode.left) + self.evaluate(tnode.right))
            elif operator == '-':
                return (self.evaluate(tnode.left) - self.evaluate(tnode.right))
            elif operator == '*':
                return (self.evaluate(tnode.left) * self.evaluate(tnode.right))
            elif operator == '/':
                right_val = self.evaluate(tnode.right)
                if right_val == 0 or not right_val:
                    raise Exception('divisor can not be 0')
                else:
                    return (self.evaluate(tnode.left) / self.evaluate(tnode.right))

    def print_tree(self, tnode, tstring):
        if tnode:
            self.print_tree(tnode.left, tstring)
            tstring[0] += str(tnode.value)
            self.print_tree(tnode.right, tstring)
