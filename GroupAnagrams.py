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

        # if key is not needed, can use "_" instead
        """
        for key, value in sAnagrams.iteritems():
            ans.append(value)
        # ans == sAnagrams.values()
        """

        #for key in sAnagrams:
        #    ans.append(sAnagrams[key])

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
