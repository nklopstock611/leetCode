# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what
# the number is. When your friend makes a guess, you provide a hint
# with the following info:

# The number of "bulls", which are digits in the guess that are in the
# correct position.
# The number of "cows", which are digits in the guess that are in your
# secret number but are located in the wrong position. Specifically,
# the non-bull digits in the guess that could be rearranged such that
# they become bulls.
# Given the secret number secret and your friend's guess guess, return
# the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls
# and y is the number of cows. Note that both secret and guess may contain
# duplicate digits.

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"

# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B" 

class Solution:
    
    def bull(self, secret: str, guess: str) -> int:
        same = 0
        h = {}
        for i, val in enumerate(secret):
            if val == guess[i]:
                same += 1
                if val not in h:
                    h[val] = 1
                else:
                    h[val] += 1

        return same, h

    def timesIn(self, s: str) -> dict:
        h = {}

        for val in s:
            if val not in h:
                h[val] = 1
            else:
                h[val] += 1

        return h

    def cow(self, secret: str, guess: str) -> int:
        cows = 0
        hs = self.timesIn(secret)
        hg = self.timesIn(guess)
        reps = {}
        bulls = self.bull(secret, guess)

        for val in guess:
            if val in hs and val in hg:

                if val not in reps:
                    reps[val] = 1
                else:
                    if reps[val] == hs[val]:
                        continue
                
                # significa que es de los repetidos.
                if val in bulls[1]:
                    if hs[val] - bulls[1][val] == 0:
                        continue
                    elif hg[val] - bulls[1][val] > 0:
                        cows += 1
                        hg[val] -= (hg[val] - bulls[1][val])
                else:
                    cows += 1

        return cows
                    
    def getHint(self, secret: str, guess: str) -> str:
        bulls = self.bull(secret, guess)
        cows = self.cow(secret, guess)
        solution = str(bulls[0]) + "A" + str(cows) + "B"
        return solution

    
sol = Solution()
secret = "8578605648"
guess =  "3675352465"
print(sol.getHint(secret, guess))