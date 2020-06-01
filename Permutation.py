"""
LeetCode 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie. sorted in ascending order).

"""

class Permutation(object):

    permutation = set()
    # Node: set() is pass-by-value, not by-reference

    def permute(self, nums):
        # type nums: list[int]
        # rtype: list[int]
        N = len(nums)
        self.permute_helper(nums, 0, N - 1)
        return list(self.permutation)

    def permute_helper(self, nums, l_idx, r_idx):
        if l_idx == r_idx:
            s = str(nums) # convert nums(list[int]) to a string
            self.permutation = self.permutation.union(set([s]))
        else:
            for i in range(l_idx, r_idx + 1):
                # swap nums[i] and nums[l_idx]
                nums[i], nums[l_idx] = nums[l_idx], nums[i] # in-place swap
                #tmp = nums[i]
                #nums[i] = nums[l_idx]
                #nums[l_idx] = tmp

                self.permute_helper(nums, l_idx + 1, r_idx)

                # swap them back
                nums[i], nums[l_idx] = nums[l_idx], nums[i] # in-place swap

    def get_next(self, nums):
        """
        find where the descent starts -> or ascent ends from back of the list
        for example, 21543 -> 2-1-543
        the descent starts after index [1]
        we want to swap nums[1] with the smallest larger than nums[1] number in list 543
        and reverse the rest and swapped 543
        2 1 543 -> 2 3 541 -> 2 3 145 -> 23145

        time complexity: O(n), where n is the length of the number array
        """
        if not nums:
            return []

        if len(nums) == 1:
            return nums

        N = len(nums)

        # find where the descent starts
        idx = -1
        for i in range(N-2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            nums.reverse()
            return nums

        # find the smallest larger than nums[idx] number
        sIdx = idx + 1
        for i in range(idx + 1, N):
            if nums[i] > nums[idx] and nums[i] <= nums[sIdx]:
                sIdx = i

        # swap
        nums[idx], nums[sIdx] = nums[sIdx], nums[idx]

        # reverse the nums from idx+1 to N-1
        # since nums[idx+1] to nums[N-1] is sorted (descent)
        endIdx = (int)((idx + 1 + N) / 2)
        count = 1
        for i in range(idx + 1, endIdx):
            nums[i], nums[N - count] = nums[N - count], nums[i]
            count += 1

        return nums

def main():
    N = 3
    nums = [i + 1 for i in range(N)]

    perm_obj = Permutation()
    permutation = perm_obj.permute(nums)
    print(permutation)

    nums2 = [[], [1], [1, 1], [1, 5, 1], [1, 3, 2], [5, 4, 3, 2, 1], [2, 1, 3, 5, 4]]
    for num in nums2:
        print('nums = {0}'.format(num))
        next_per = perm_obj.get_next(num)
        print(next_per)

if __name__ == '__main__':
    main()
