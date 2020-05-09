"""
LeetCode 26. Remove Duplicates from Sorted array

Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory

"""

class SortedArray(object):

    def remove_duplicates(self, nums):
        # type nums: List[int]
        # rtype: int
        if not nums:
            return 0

        target_num = nums[0]
        next_idx = 1
        N = len(nums)
        i = 1
        while i < N:
            num = nums[i]
            if num == target_num:
                i += 1
            else:
                nums[next_idx] = num
                next_idx += 1
                target_num = num

        ans = [num for num in nums[:next_idx]]

        return ans

        """
        # faster than 99.55% of Python online solution
        
        i = 0
        N = len(nums)
        for j in range(1, N):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
        """

def main():
    num_arrays = [ [1, 1], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]

    for nums in num_arrays:
        print('input number array: {0}'.format(nums))
        obj = SortedArray()
        single_nums = obj.remove_duplicates(nums)
        print('remove duplicates, new array: {0}'.format(single_nums))
        print('remove duplicates, new length: {0}'.format(len(single_nums)))

if __name__ == '__main__':
    main()
