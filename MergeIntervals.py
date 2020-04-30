"""
LeetCode 56. Merge Intervals
"""

class MergeIntervals():

    def merge(self, intervals):

        """
        type list_nums: List[List[int]]
        rtype: List[List[int]]

        Sort the intervals by start point and then end point
        And then can limit the comparison to only with the previous interval
        """
        if not intervals:
            return None

        ans = [] # Initialization for list

        # Sort intervals
        intervals.sort()
        #self.qsort_intervals(intervals, 0, len(intervals) - 1)
        print("After sorting, {}".format(intervals))

        for int_item in intervals:
            if not ans:
                ans.append(int_item)
            else:
                idx = len(ans) - 1
                if int_item[0] <= ans[idx][1]:
                    # Intervals have overlap
                    ans[idx][1] = max(int_item[1], ans[idx][1])
                else:
                    ans.append(int_item)

        return ans

    def qsort_intervals(self, list_nums, low, high):
        if low < high:
            # pivot is partitioning index
            # list_nums[pivot] is now at right place
            pivot = self.partition(list_nums, low, high)
            print("pivot: {}, array: {}".format(pivot, list_nums))
            self.qsort_intervals(list_nums, low, pivot - 1)
            self.qsort_intervals(list_nums, pivot + 1, high)

    def partition(self, list_nums, low, high):
        # Pivot: element to be placed at right position
        pivot = list_nums[high]

        sm_idx = low # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than the pivot
            if self.smaller(list_nums[j], pivot):
                tmp_num = list_nums[j]
                list_nums[j] = list_nums[sm_idx]
                list_nums[sm_idx] = tmp_num
                sm_idx += 1

        tmp_num = list_nums[sm_idx]
        list_nums[sm_idx] = list_nums[high]
        list_nums[high] = tmp_num

        return sm_idx

    def smaller(self, int_a, int_b):
        if (int_a[0] < int_b[0]):
            return True
        elif (int_a[0] == int_b[0] and int_a[1] < int_b[1]):
            return True
        else:
            return False


def main():

    array = [[2, 5], [1, 4], [3, 6], [2, 7], [15, 20]]
    #array = [[1, 10], [4, 10], [3, 10], [8, 10], [2, 10], [10, 10]]
    print(array)
    merge_int = MergeIntervals()
    ans = merge_int.merge(array)
    print(ans)

if __name__ == '__main__':
    main()
