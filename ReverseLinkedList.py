"""
LeetCode 206. Reverse Linked List

Reverse a singly linked list

"""

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
    @property
    def val(self):
        if not self:
            return None
        return self.val

    @val.setter
    def val(self, val):
        self.val = val

    @property
    def next(self):
        if not self:
            return None
        return self.next

    @next.setter
    def next(self, next):
        self.next = next
"""

class LinkedList(object):

    def __init__(self):
        self.head = None

    def create(self, array):
        cr_node = None
        for i in array[::-1]:
            new_node = ListNode(i, cr_node)
            cr_node = new_node

        self.head = cr_node

        return self.head

    def print_list(self):
        string = 'Linked list: '

        if self.head:
            string += str(self.head.val)
            node = self.head.next

            while node:
                string += ("->" + str(node.val))
                node = node.next

        print(string)

    def reverse(self, head):
        if not self.head:
            return None

        cr_node = ListNode(self.head.val, None)
        node = self.head.next

        while node:
            new_node = ListNode(node.val, cr_node)
            cr_node = new_node
            node = node.next

        self.head = cr_node

    def reverse_between(self, head, m, n):
        # reverse a linked list between m to n
        # m and n are indexes
        if not self.head or m >= n:
            return

        pre_node = None
        if m == 1:
            pre_node = self.head

        tail_node = None
        cr_node = None
        count = 1

        node = self.head
        while node and count <= n:
            if count == m - 1:
                pre_node = node

            if count >= m and count <= n:
                if count == m:
                    tail_node = node
                    cr_node = node
                else:
                    new_node = ListNode(node.val, cr_node)
                    cr_node = new_node

            count += 1
            node = node.next

        if m == 1:
            self.head = cr_node
        else:
            pre_node.next = cr_node

        tail_node.next = node

def main():
    array = [3, 5] #[1, 2, 3, 4, 5]
    linkedList = LinkedList()

    print('Original linked list:')
    head = linkedList.create(array)
    linkedList.print_list()

    print('Reverse linked list:')
    linkedList.reverse(head)
    linkedList.print_list()

    m = 1
    n = 2
    print('Reverse linked list between {0} and {1}:'.format(m, n))
    linkedList.reverse_between(head, m, n)
    linkedList.print_list()

if __name__ == '__main__':
    main()
