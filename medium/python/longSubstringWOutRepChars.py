class Solution:

    def maxInList(self, l: list) -> int:
        max = 0
        for val in l:
            if val >= max:
                max = val
        
        return max

    def uniqueChars(self, s: str) -> bool:
        b = True
        d = {}
        for val in s:
            if val not in d:
                d[val] = None

        if len(d) != len(s):
            b = False

        return b

    def retrieveNotReps(self, rep: str, d: dict) -> dict:
        h = {}
        for val in d:
            if val != rep:
                h[val] = None

        return h

    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        c = 0
        r = []

        b = self.uniqueChars(s)

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif b:
            return len(s)

        for i, val in enumerate(s):
            if val not in d:
                d[val] = None
                c += 1
                if i == len(s) - 1:
                    r.append(c)
            else:   
                r.append(c)
                c = 0
                d = self.retrieveNotReps(val, d) # revisar esta lógica!
                c += len(d)
                d[val] = None
                c += 1

        return self.maxInList(r)

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
