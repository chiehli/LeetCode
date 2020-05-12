"""
LeetCode 561. Array Partition I

given an array of 2n integers, group these integers into n pairs of integer,
which makes sum of min(ai, bi) for all i from 1 to n as large as possible

"""

class ArrayPairSum(object):

    def find_max_min_sum(self, nums):
        """
        Thoughts:
        Pair the max and second max so that we can include second max in our answer,
        where second max is the max value to contribute to a bigger sum

        So sort the integer array first and group the adjacent numbers as a pair,
        sum the smaller one

        runtime: 248 ms, faster than 96.86% of Python online submission
        memory usage: 15.2 MB, less than 6.06% of Python online submission
        """

        if not nums:
            return 0

        nums.sort()

        ans = 0
        N = len(nums)

        for i in range(0, N, 2): # increment by 2
            ans += nums[i]

        return ans

def main():
    nums = [1, 4, 2, 3]
    obj = ArrayPairSum()

    print(nums)
    print('find max sum of min value in pair:')
    print(obj.find_max_min_sum(nums))

if __name__ == '__main__':
    main()
