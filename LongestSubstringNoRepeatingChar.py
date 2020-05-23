"""
LeetCode 3. Longest Substring without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters

Example 1:
Input: "abcabcbb"
Output: 3 ("abc")

Example 2:
Input: "pwwkew"
Output: 3 ("wke")

"""

class LongestSubstring(object):

    def get_length(self, s):
        # type s: str
        # rtype: int

        #ans_str = []
        #ans_str.append('')
        #max_sub_length = self.recur_get_len_helper(s, ans_str)
        #print(ans_str[0])

        max_sub_length = self.sliding_window_optimized(s)
        return max_sub_length

    def sliding_window_helper(self, s):
        """
        substr_ij indicates the substring without repeat letters from index i to index j
        check if the letter at index j+1 has repeated letter

        if yes, compare length of current substring with the max_length and update as needed
        else, continuing sliding the window -> j += 1

        Time complexity: O(n)
        """
        dict = {}
        substr = ''
        max_length = 0
        max_str = ''

        i = 0
        j = i
        while i < len(s) and j < len(s):
            if s[j] not in dict:
                dict[s[j]] = j
                substr += s[j]
                j += 1
            else:
                if len(substr) > max_length:
                    max_length = len(substr)
                    max_str = substr
                substr = ''
                i += 1
                j = i
                dict = {}

        if len(substr) > max_length:
            max_length = len(substr)
            max_str = substr

        print("max_substr = {0}".format(max_str))
        return max_length

    def sliding_window_optimized(self, s):
        """
        substr_ij indicates the substring without repeat letters from
        index i to index j
        check if the letter at index j+1 has repeated letter

        if yes, compare length of current substring with the max_length
        and update as needed
        next, update substr_ij as substr_idx+1_j where idx is the index the
        repeated character appears
        else, continuing sliding the window -> j += 1

        Time complexity: O(n)
        """
        dict = {}
        max_length = 0

        i = 0 # start from the beginning
        j = i
        N = len(s)

        while i < N and j < N:
            if s[j] not in dict:
                # no repeat, continue adding j
                dict[s[j]] = j
                j += 1
            else:
                if len(dict) > max_length:
                    # check if current substring has longer length
                    max_length = len(dict)

                idx = dict[s[j]]
                for k in range(i, idx):
                    # update dictionary
                    # remove the character from s[i] to s[idx - 1]
                    # because we are going to look at a new substring
                    if s[k] in dict:
                        del dict[s[k]]

                dict[s[j]] = j # update the index where s[j] appears
                i = idx + 1
                j += 1

        dict_length = len(dict)
        if dict_length > max_length:
            max_length = dict_length

        return max_length

    def recur_get_len_helper(self, s, ans):
        # Time complexity: O(n^3)
        dict = {}

        for i, char in enumerate(s):
            if char not in dict:
                dict[char] = i
            else:
                index = dict[char]
                return max(self.recur_get_len_helper(s[0 : i], ans),
                        self.recur_get_len_helper(s[index + 1 : len(str)], ans))

        if len(s) > len(ans[0]):
            ans[0] = s

        return len(ans[0])

def main():
    strs = ["aabaab!bb", "bb", "abcabcbb", "pwwkew"]#["abcabcbb", "pwwkew"]
    obj = LongestSubstring()

    for str in strs:
        print('string = {0}'.format(str))
        longest_length = obj.get_length(str)
        print('longest substring length: {0}'.format(longest_length))

if __name__ == '__main__':
    main()
