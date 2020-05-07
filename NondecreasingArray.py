"""
LeetCode 665. Non-decreasing array

Given an array nums with n integers, check if it could become non-decreasing
by modifying at most 1 element

Non-decreasing: nums[i] <= nums[i + 1] for every i (0-based) such that 0 <= i <= n-2

"""

class NondecreasingArray(object):

    def checkPossibility(self, nums):
        # type nums: List[int]
        # rtype: bool

        if not nums:
            return False

        N = len(nums)
        p = -1 # init

        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                if p != -1:
                    return False
                p = i

        if p <= 0 or p == N - 2:
            # p <= 0: the nums is already a non-decreasing array or the change happens at the first element
            # p == N - 2: the change happens at the last element
            return True

        if nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]:
            # change happens at the middle of the array
            # check its neighbors
            return True

def main():
    nums = [[1, 2, 3], [4, 2, 3], [3, 4, 2, 3]]

    obj = NondecreasingArray()
    for num in nums:
        print(num)
        print("Non-decreasing array: {0}".format(obj.checkPossibility(num)))

if __name__ == '__main__':
    main()
