"""
LeetCode 384. Shuffle an array

Shuffle a set of numbers without duplicates
"""
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self._oriNums = [num for num in nums] # make a copy

    def reset(self):
        """
        Resets the array to its original configuration and return it
        :rtype: List[int]
        """
        return self._oriNums


    def shuffle_in_place(self):
        """
        Returns a random shuffling of the array
        :rtype: List[int]
        """

        # randomly select a number between 0 - N-1 (the length of the array)
        # swap the selected element with the last element in the array
        # reduce the array length by 1 each time and repeat the randomly select

        N = len(self._nums)
        print(N)
        #random.seed() # the one that takes time

        while N > 0:
            rnd = random.randint(0, N - 1)
            tmp = self._nums[rnd]
            self._nums[rnd] = self._nums[N - 1]
            self._nums[N - 1] = tmp
            N -= 1
            # print('select: {0}, new_array: {1}'.format(rnd, self._nums))

        return self._nums

    def shuffle(self):
        aus = list(self._nums)

        size = len(self._nums)
        for idx in range(size):
            removed_idx = random.randrange(len(aus))
            self._nums[idx] = aus.pop(removed_idx)
            # list.pop(item_idx) <- remove and pop the indexed item

        return self._nums

def main():
    nums = ['1', '2', '3', '4', '5', '6']
    print('input array: {0}'.format(nums))
    obj = Solution(nums)
    print('shuffle array: {0}'.format(obj.shuffle()))
    print('reset array: {0}'.format(obj.reset()))

if __name__ == '__main__':
    main()
