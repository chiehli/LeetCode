"""
A class of trie tree
"""

class TrieNode(object):
    _AlphaSize = 26

    def __init__(self):
        self._children = [None] * self._AlphaSize
        self._isEndOfWord = False

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    @property
    def isEndOfWord(self):
        return self._isEndOfWord

    @isEndOfWord.setter
    def isEndOfWord(self, endFlag):
        self._isEndOfWord = endFlag


class TrieTree(object):
    _AlphaSize = 26

    def __init__(self):
        self._root = self.get_node()

    def get_node(self):
        # return a new trie node
        return TrieNode()

    def _char_to_index(self, ch):
        # private helper function
        # converts key current character into index
        # use only 'a' through 'z' and lower case

        # ord(): returns an int representing the Unicode character
        return ord(ch) - ord('a')

    def _index_to_char(self, index):
        # private helper function
        # converts index into character into

        # chr(): returns a char (or a string) from an integer (Unicode character)
        return chr(ord('a') + index)

    def insert(self, word):
        if not self.search(word):
            parentNode = self._root

            for char in word:
                index = self._char_to_index(char)

                # if current character is not present
                if not parentNode.children[index]:
                    parentNode.children[index] = self.get_node()
                parentNode = parentNode.children[index]

            # mark last node as leaf
            parentNode.isEndOfWord = True

    def remove(self, word):
        if not self._root:
            return None

        # word is not in the trie tree
        if not self.search(word):
            return self._root

        self.remove_helper(self._root, word, 0)

    def remove_helper(self, trieNode, word, depth=0):
        # if last character of word is being processed
        if depth == len(word):
            # this node is not the end of word after remove current word
            if trieNode.isEndOfWord:
                trieNode.isEndOfWord = False

            # if given is not prefix of any other word
            if self.is_empty(trieNode):
                trieNode = None

            return self._root

        # if not last character, recur for the child
        index = self._char_to_index(word[depth])
        self.remove_helper(trieNode.children[index], word, depth + 1)

        # if root does not have any child (its only child got deleted)
        # and it is not end of another word
        if self.is_empty(trieNode) and not trieNode.isEndOfWord:
            trieNode = None

        return self._root

    def is_empty(self, trieNode):
        # return true if trieNode has no children
        # else false

        for i in range(self._AlphaSize):
            if trieNode.children[i]:
                return False
        return True

    def search(self, word):
        parentNode = self._root

        for char in word:
            index = self._char_to_index(char)
            if not parentNode.children[index]:
                return False
            else:
                parentNode = parentNode.children[index]

        if parentNode != None and parentNode.isEndOfWord:
            return True
        else:
            return False

    def display(self):
        word = []
        self.display_helper(self._root, word)

    def display_helper(self, trieNode, word):
        if trieNode and trieNode.isEndOfWord:
            print("".join(word)) # print(str(word)) works too!
            return
        else:
            for i in range(self._AlphaSize):
                if trieNode.children[i]:
                    word.append(self._index_to_char(i))
                    self.display_helper(trieNode.children[i], word)
                    word.pop(-1)
