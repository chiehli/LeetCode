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
        secretTable = {}
        guessTable = {}
        for i in range(len(secret)):
            gDigit = guess[i]
            sDigit = secret[i]
            if gDigit == sDigit:
                # Digits match
                # Bulls (A) increment
                bullCount += 1
            else:
                # Digits do not match
                # Add the not matched digits to corresponding hash table
                if sDigit in secretTable:
                    secretTable[sDigit] += 1
                else:
                    secretTable[sDigit] = 1
                if gDigit in guessTable:
                    guessTable[gDigit] += 1
                else:
                    guessTable[gDigit] = 1

        # Check the number of Cows (B)
        for num in guessTable:
            gCount = guessTable[num]
            if num in secretTable:
                sCount = secretTable[num]
                cowCount += min(gCount, sCount)

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

    guess = ''
    print('guess: ' + guess)
    print(bull_n_cow.getHint(secret, guess))

if __name__ == '__main__':
    main()
