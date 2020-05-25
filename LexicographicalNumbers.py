"""
LeetCode 386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order
For example, given 13, return [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

"""

class LexicographicalNumbers(object):

    def get_lexical_order(self, n):
        # type n: int
        # rtype: list[int]

        # create a string array consisting of numbers from 1 to n
        str_arr = [str(i + 1) for i in range(0, n)]
        str_arr.sort()

        # after sorting, convert the string array to integer array
        ans_arr = [int(s) for s in str_arr]
        return ans_arr

def main():
    n = 13
    obj = LexicographicalNumbers()
    ans = obj.get_lexical_order(n)
    print('Lexicographical order: {0}'.format(ans))

if __name__ == '__main__':
    main()
