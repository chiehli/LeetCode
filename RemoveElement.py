"""
LeetCode 27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place
and return the new length

"""

class ArrayElements(object):

    def removeElement(self, nums, val):
        if not nums:
            return 0

        N = len(nums)
        i = 0
        j = N - 1 # point to the next position from back of the nums of num not equaling to val

        while j >= 0:
            if nums[j] == val:
                j -= 1
            else:
                break

        if j < 0:
            return 0

        while i < j and i < N and j >= 0:
            if nums[i] == val:
                tmp = nums[j]
                nums[j] = val
                nums[i] = tmp

                while j >= 0:
                    if nums[j] == val:
                        j -= 1
                    else:
                        break
            else:
                i += 1

        print(nums)

        """
        i = 0

        for j in range(N):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

        """

        return i + 1

def main():
    nums = [[1], [0, 1, 2, 2, 3, 0, 4, 2], [3, 2, 2, 3]]
    vals = [1, 2, 3]
    obj = ArrayElements()

    for i in range(len(nums)):
        print('nums = {0}, val = {1}'.format(nums[i], vals[i]))
        length = obj.removeElement(nums[i], vals[i])
        print('after removing elements, length = {0}'.format(length))

if __name__ == '__main__':
    main()
