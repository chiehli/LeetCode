"""
1247. Minimum Swaps to Make Strings Equal

Find the minimum number of swaps requried to make string1 and string2 equals
Return -1 if it is impossible to do so
string1 and string2 only consist letters 'x' and 'y'

"""

class StringOperation(object):
    def find_min_swaps(self, str1, str2):
        if len(str1) != len(str2):
            return -1

        x_count = 0
        res_str1 = ''

        # go through str1 and str2
        # we can ignore for letters those are the same in str1 and strs2
        # only get those letters those are diff from str1 to str2, store in res_str1
        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            if c1 != c2:
                res_str1 += c1
                if c1 == 'x':
                    x_count += 1

        res_len = len(res_str1)

        # if number of letters in res_str1 is an odd numbers
        # then it is impossible to make str1 and str2 equal
        if res_len % 2 == 1:
            return -1


        # if s1 = 'xx' and s2 = 'yy', then one swap can make them equal
        # if s1 = 'xy' and s2 = 'yx', then we need two swaps
        y_count = res_len - x_count

        # count how many xx and yy pairs in res_str1
        # and how many xy pairs left
        swap_count = x_count / 2 + (y_count) / 2 + x_count % 2 + y_count % 2

        return swap_count

def main():
    strs1 = ['xyyyyx', 'yyy', 'xy', 'xx', 'xxy']
    strs2 = ['xxxxyy', 'yyy', 'yx', 'yy', 'yyx']
    str_obj = StringOperation()

    for i in range(len(strs1)):
        print(strs1[i])
        print(strs2[i])
        swap_num = str_obj.find_min_swaps(strs1[i], strs2[i])
        print('minimum swaps: {0}'.format(swap_num))

if __name__ == '__main__':
    main()
