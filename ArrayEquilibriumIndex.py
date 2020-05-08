"""
Equilibrium Index of An Array

Equilibrium index of an array is an index subh that the sum of elements at lower
indexes is equal to the sum of elements at higher indexes

"""

class EquilibriumIndex(object):

    def find(self, nums):
        # type nums: List[int]
        # rtype: int
        if not nums:
            return None

        N = len(nums)
        # get the sum of the entire integer array
        total_sum = 0
        for num in nums:
            total_sum += num

        # the next step is to see if excluding current index
        # the sum of elements at lower indexes is equal to the sum of elements at high indexes
        ans_idxes = []
        lower_sum = 0
        target_val = total_sum - nums[0]

        """
        if lower_sum == target_val:
            ans_idx = 0

        for i in range(1, N):
            lower_sum += nums[i - 1]
            target_val = (total_sum - nums[i]) / 2

            if lower_sum == target_val:
                ans_idxes.append(i)
        """

        # practice enumerate
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums): # practice enumerate
            total_sum -= num # now total_sum is the right sum
            if left_sum == total_sum:
                ans_idxes.append(i)

            left_sum += num # update for next round

        return ans_idxes

def main():
    nums = [-7, 1, 5, 2, -4, 3, 0]
    obj = EquilibriumIndex()
    print('nums: {0}'.format(nums))
    print('equilibritum index at {0}'.format(obj.find(nums)))

if __name__ == '__main__':
    main()
