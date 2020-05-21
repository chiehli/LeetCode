"""
LeetCode 78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set)

Example:
Input nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

"""

class Subset(object):

    def find_power_set(self, nums):
        if not nums:
            return []

        buffer = []
        ans = []
        ans.append([])

        self.find_power_set_helper(nums, buffer, 0, ans)
        return ans

    def find_power_set_helper(self, nums, buffer, index, ans):
        if index >= len(nums):
            return

        buffer.append(nums[index])
        ans.append(list(buffer))
        #print('i = {0}, buffer = {1}, ans = {2}'.format(index, buffer, ans))
        self.find_power_set_helper(nums, buffer, index + 1, ans)
        buffer.pop(-1) # pop out nums[index] -> without nums[index]
        self.find_power_set_helper(nums, buffer, index + 1, ans)

def main():
    N = 3
    nums = [i + 1 for i in range(N)]
    print('nums = {0}'.format(nums))

    set = Subset()
    print(set.find_power_set(nums))

if __name__ == '__main__':
    main()
