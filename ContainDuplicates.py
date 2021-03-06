"""
LeetCode 217. Contains duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
"""

class ContainDuplicates():

    def check(self, array):
        """
        type array: List[int]
        rtype: bool
        """
        if not array:
            return False

        table = {} # table = dict()
        for num in array:
            if num in table:
                return True
            else:
                table[num] = 1
        return False


def main():
    array = [1, 2]
    contain_dupe = ContainDuplicates()
    print(array)
    print(contain_dupe.check(array))

    array = []
    print(array)
    print(contain_dupe.check(array))

    array = [2, 3, 2]
    print(array)
    print(contain_dupe.check(array))


if __name__ == '__main__':
    main()
