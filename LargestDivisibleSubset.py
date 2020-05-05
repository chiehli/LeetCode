"""
LeetCode 368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satifies:

Si % Sj = 0, Si > Sj

If there are multiple solutions, return any subset is fine
"""
import math

class DivisibleSubset(object):

    def largest_divisible_subset(self, nums):
        # type nums: List[int]
        # rtype: List[int]

        # Time complexity: O(n^2)
        # Auxiliary space: O(n)

        if not nums:
            return []

        # sort the nums array so that all divisors of an element are before it
        nums.sort(reverse = False)
        # or nums = sorted(nums)

        N = len(nums)
        divCount = [1 for i in range(N)]
        # to store the number of divisors for each element, init with 1
        # because element will always be a factor of itself

        prev = [-1 for i in range(N)]
        # to store previous divisor in result

        max_idx = 0
        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if divCount[i] < divCount[j] + 1:
                        divCount[i] = divCount[j] + 1
                        prev[i] = j

            # update last index of largest subset if size of current subset is more
            if divCount[max_idx] < divCount[i]:
                max_idx = i

        max_subset = []
        prev_idx = max_idx
        while prev_idx >= 0:
            max_subset.append(nums[prev_idx])
            prev_idx = prev[prev_idx]

        max_subset.sort()

        return max_subset

def main():
    nums = [1, 2, 3, 6, 7, 14, 28]
    obj = DivisibleSubset()
    print('number array: {0}'.format(nums))
    print('largest divisible subset: {0}'.format(obj.largest_divisible_subset(nums)))

if __name__ == '__main__':
    main()
