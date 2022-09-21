# https://leetcode.com/problems/isomorphic-strings/

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can
# be replaced to get t.
# All occurrences of a character must be replaced with another
# character while preserving the order of characters. No two characters
# may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        h_s_t = {}
        h_t_s = {}

        for i in range(len(s)):
            # se van asignando valores correspondientes.
            if s[i] not in h_s_t and t[i] not in h_t_s:
                h_s_t[s[i]] = t[i]
                h_t_s[t[i]] = s[i]
            # algo parecido a revisar si están en la misma posición.
            elif h_s_t.get(s[i]) != t[i] or h_t_s.get(t[i]) != s[i]:
                return False

        return True


# Main
sol = Solution()
s = "egg"
t = "add"
print(sol.isIsomorphic(s, t))