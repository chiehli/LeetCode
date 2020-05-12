"""
LeetCode 11. Container With Most Water

"""
import math

class Container(object):

    def max_water_volume(self, heights):
        # type nums: List[int]
        # rtype: int

        # greedy algorithm

        """
        Thoughts:
            Start with the left most and right most indexes
            Calculate its area (init water volume)
            Next, move only the lower value index toward center and get the area
             every time until the left index and right index meet each other
        """

        if not heights:
            return 0

        N = len(heights)

        # init
        left_idx = 0 #0 if heights[0] > heights[1] else 1
        left_val = heights[left_idx]
        right_idx = N - 1
        right_val = heights[right_idx]
        maxArea = (right_idx - left_idx) * min(left_val, right_val)

        ans_left = 0
        ans_right = 0

        while left_idx < right_idx:
            left_val = heights[left_idx]
            right_val = heights[right_idx]
            area = (right_idx - left_idx) * min(left_val, right_val)

            if area > maxArea:
                maxArea = area
                ans_left = left_idx
                ans_right = right_idx

            if right_val < left_val:
                right_idx -= 1
            else:
                left_idx += 1

        print('left index: heights[{0}] = {1}, right index: heights[{2}] = {3}'.format(ans_left, heights[ans_left], ans_right, heights[ans_right]))
        print('maxArea = {0}'.format(maxArea))
        return maxArea

def main():
    heights_array = [[1, 1], [1, 2, 4, 3], [1, 8, 6, 2, 5, 4, 8, 3, 7]]

    obj = Container()
    for heights in heights_array:
        print('heights = {0}'.format(heights))
        obj.max_water_volume(heights)

if __name__ == '__main__':
    main()
