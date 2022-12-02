class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_inv = s[::-1]
        length = 0
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(s_inv)):
            if s_inv[i] in letters:
                length += 1
                if s_inv[i + 1] == " ":
                    print(length)
                    break

        return length

sol = Solution()
s = "Hello World"
print(sol.lengthOfLastWord(s))