"""
LeetCode 49. Group Anagrams

Given an array of string, group anagrams together.

Example:
Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output:
[
    ['ate', 'eat', 'tea'],
    ['nat', 'tan'],
    ['bat']
]

"""

class Anagrams(object):

    def group(self, strings):
        # time complexity: n * klogk, where n is the number in strings
        # and k is the average length of individual string
        # time complexity will be O(n) if n >> k
        # or O(klogk) if k >> n

        if not strings:
            return [] #

        sAnagrams = {}
        for string in strings:
            s = sorted(string) # sorted() will return a list!
            sortedStr = "".join(s) # concatenante sorted char list back to str

            if sortedStr not in sAnagrams:
                sAnagrams[sortedStr] = [string]
            else:
                sAnagrams[sortedStr].append(string)

        ans = []
        for _, val in sAnagrams.iteritems():
            ans.append(val)

        """
        Explanation for code in lines 39-40

        - The original code is:

        for key in sAnagrams:
            ans.append(sAnagrams[key])

        - Because sAnagrams is a dictionary, we can also write as:

        for key, val in sAnagrams.iteritems():
            ans.append(val)

        - Since the values of keys are not used, we can use "_" instead:

        for _, val in sAnagrams.iteritems():
            ans.append(val)

        - We can also get all the values in a dictionary by using the '.values()'

        ans == sAnagrams.values()
        """

        return ans

"""
If k >> n, we may want to remove sorting string from the method.
We can build a hash table for individual string and compare the key-value pair
in hash tables are equal or not.
If equal -> anagrams
"""

def main():
    strings = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print('Strings: {0}'.format(strings))
    obj = Anagrams()
    grouping = obj.group(strings)
    print('After grouping: {0}'.format(grouping))

if __name__ == '__main__':
    main()
