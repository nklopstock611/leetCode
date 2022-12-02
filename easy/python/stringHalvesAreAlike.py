class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        n = len(s)
        first = s[:int(n/2)]
        second = s[int(n/2):]

        v = 0
        for i in range(int(n/2)):
            if first[i] in vowels:
                v += 1
            if second[i] in vowels:
                v -= 1

        b = False
        if v == 0:
            b = True

        return b

sol = Solution()
s = "textbook"
print(sol.halvesAreAlike(s))