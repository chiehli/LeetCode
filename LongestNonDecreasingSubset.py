"""
Longest Non-Decreasing Subset

Given an unsorted integer array, find the longest non-decreasing subset
"""

class NonDecreasingSubset(object):

    def longest_subset(self, nums):
        if not nums:
            return [] # not nums, return an empty subset

        N = len(nums)
        subsetCount = [1 for i in range(N)]
        prev = [-1 for i in range(N)]

        max_idx = 0
        for i in range(1, N):
            for j in range(i):
                if nums[i] >= nums[j] and subsetCount[i] < subsetCount[j] + 1:
                    subsetCount[i] = subsetCount[j] + 1
                    prev[i] = j

            if subsetCount[max_idx] < subsetCount[i]:
                max_idx = i

        idx = max_idx
        longest_subset = []
        while idx >= 0:
            longest_subset.append(nums[idx])
            idx = prev[idx]

        longest_subset.sort()
        return longest_subset

def main():
    nums = [7, 4, 2, 3, 5, 10, 11, 12, 18]
    #nums = [7, 6, 5, 4, 3, 2, 1]
    print('input array: {0}'.format(nums))
    obj = NonDecreasingSubset()
    print('find one of its longest non-decreasing subsets: {0}'.format(obj.longest_subset(nums)))

if __name__ == '__main__':
    main()
