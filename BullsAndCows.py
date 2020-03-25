"""
LeetCode 299. Bulls and Cows

xAxB game!
"""

class BullsAndCows():

    def getHint(self, secret, guess):
        """
        type secret: str
        type guess: str
        rtype: str
        """
        if not secret or not guess:
            raise Exception('invalid inputs')

        bullCount = 0
        cowCount = 0
        table = {}
        for i in range(len(secret)):
            gDigit = guess[i]
            sDigit = secret[i]
            if gDigit == sDigit:
                # Digits match
                # Bulls (A) increment
                bullCount += 1
            else:
                # Digits do not match
                # Add the not matched digits to table and update cowCount
                # if is sDigit, table[sDigit] += 1,
                # if is gDigit, table[gDigit] -= 1
                # if table[sDigit] < 0 -> the digit appears in guess, 
                # -> cowCount += 1
                # if table[gDigit] > 0 -> the digit appears in secret,
                # -> cowCount += 1
                if sDigit in table:
                    if table[sDigit] < 0:
                        cowCount += 1
                    table[sDigit] += 1
                else:
                    table[sDigit] = 1
                if gDigit in table:
                    if table[gDigit] > 0:
                        cowCount += 1
                    table[gDigit] -= 1
                else:
                    table[gDigit] = -1

        ans = '{0}A{1}B'.format(bullCount, cowCount)
        return ans


def main():
    secret = '0707'
    guess = '1234'

    bull_n_cow = BullsAndCows()
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

    guess = '7700'
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

    guess = '0707'
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

    secret = '1123'
    guess = '0111'
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

    guess = ''
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

if __name__ == '__main__':
    main()
