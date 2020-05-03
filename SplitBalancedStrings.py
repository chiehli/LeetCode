"""
LeetCode 1221. Split a String in Balanced Strings

"""

class StringOperation(object):
    def split_in_balanced_strings(self, input_str):
        if not input_str:
            return 0

        r_count = 0
        l_count = 0
        bal_str_count = 0
        bal_str = []
        sub_str = ''

        for char in input_str:
            if char == 'R':
                r_count += 1
                sub_str += 'R'
            elif char == 'L':
                l_count += 1
                sub_str += 'L'

            if r_count == l_count:
                bal_str_count += 1
                r_count = 0
                l_count = 0
                bal_str.append(sub_str)
                sub_str = ''

        print("input string: {0}, number of balanced strings: {1}".format(input_str, bal_str_count))
        print(bal_str)

        return bal_str_count

def main():
    input_str = ['RLRRLLRLRL', 'RLLLLRRRLR', 'LLLLRRRR', 'RLRRRLLRLL']
    str_obj = StringOperation()

    for str in input_str:
        str_obj.split_in_balanced_strings(str)

if __name__ == '__main__':
    main()
