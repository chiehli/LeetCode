"""
LeetCode 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width
of each bar is 1. Compute how much water it is able to trap after raining.

"""

class TrappingRainWater(object):

    def compute(self, heights):
        # type nums: list[int]
        # rtype: int

        # time complexity: 3n -> O(n), where n is the length of heights
        # space complexity: 2n -> O(n), left_max and right_max

        if not heights:
            return 0

        N = len(heights)
        left_max = [0 for i in range(N)]
        right_max = [0 for i in range(N)]

        # find the max height of bar from the left end upto an index i in the array
        left_max[0] = heights[0]
        for i in range(1, N):
            left_max[i] = max(heights[i], left_max[i - 1])

        # find the max height of bar from the right end upto an index in the array
        right_max[N - 1] = heights[N - 1]
        for i in range(N - 2, -1, -1):
            right_max[i] = max(heights[i], right_max[i + 1])

        # get the intersection
        trapped_water = 0
        for i in range(N):
            trapped_water += min(left_max[i], right_max[i]) - heights[i]

        return trapped_water

def main():
    heights_array = [[], [1], [1, 0, 1], [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
    obj = TrappingRainWater()

    for heights in heights_array:
        print('nums = {0}'.format(heights))
        water = obj.compute(heights)
        print('trapped rain water = {0}'.format(water))

if __name__ == '__main__':
    main()
