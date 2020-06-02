"""
LeetCode 319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it's off or turning off if it's on).
For the i-th round, you toggle every i bulb. For the n-th round, you only
toggle the last bulb. Find how many bulbs are on after n rounds.

"""

class BulbSwitcher(object):

    def count(self, n):
        """
        Find how many bulbs are on after n rounds
        -> Find how many square numbers less than or equal to n

        -> bulb will be on if toggled odd times
        -> i-th bulb will be toggled when current round j is a factor of i
        -> square numbers have odd number of factors (for example, 4's factors are 1, 2, 4)
        -> so we need to find out how many squre numbers are less than or equal to n
        """

        i = 1
        count = 0

        while i * i <= n:
            count += 1
            i += 1

        return count

def main():
    n = 7
    obj = BulbSwitcher()
    print('n = {0}'.format(n))
    print('numbers of bulb are on after n rounds: {0}'.format(obj.count(n)))

if __name__ == '__main__':
    main()
