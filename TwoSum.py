"""
LeetCode 1. Two Sum

Given an array of integers, return indices of the two numbers such that
they add up to a specific target

"""

class TwoSum(object):

    def find(self, nums, target):
        dict = {}
        ans = []

        # use a dictionary to store items in nums
        for i, num in enumerate(nums):
            if num not in dict:
                a = [i]
                dict[num] = a
            else:
                # for duplicate items, append the index to the existing one
                dict[num].append(i)

        #print(dict)

        for i, num in enumerate(nums):
            res = target - num

            if res == num:
                if res in dict and len(dict.get(res)) == 2:
                    ans.append(dict[res][0])
                    ans.append(dict[res][1])
                    break
            else:
                if res in dict:
                    ans.append(i)
                    ans.append(dict[res][0])
                    break

        return ans

def main():
    nums = [[2, 7, 11, 13], [3, 3], [3, 2, 4]]
    target = [9, 6, 6]

    obj = TwoSum()
    for i in range(0, len(nums)):
        print('nums = {0}, target = {1}'.format(nums[i], target[i]))
        print('integers indices: {0}'.format(obj.find(nums[i], target[i])))

if __name__ == '__main__':
    main()
