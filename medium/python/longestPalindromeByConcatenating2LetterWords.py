
def longestPalindrome(words: list) -> int:
        h = {}
        eqs = {}
        res = 0
        eq = False
        count = 0
        for val in words:
            if val not in h:
                h[val] = 1
            else:
                h[val] += 1

        for val in words:
            hvalue = h[val]
            if val[0] == val[1] and hvalue > 1:
                eqs[val] = None
            elif val[0] == val[1] and hvalue == 0:
                count += 1
                
        if count == len(words):
            eq = True

        print(h)
        for val in words:
            reversed = val[1] + val[0]
            if reversed in h:
                if eq == False:
                    res += 2
                else:
                    res = 2

        return res



words =  ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
h = {}
n = len(words)
l = words.copy()
s = []
res = 0
for val in words:
  if val not in h:
    h[val] = 1
  else:
    h[val] += 1

for val in range(n):
    reversed = words[val][1] + words[val][0]
    if words[val][0] == words[val][1]:
        if h[words[val]] >= 2:
            l.remove(words[val])
            s = l.copy()
            s.pop(s.index(words[val]))
            l = s.copy()
            res = (n * 2) - (len(l) * 2)
        elif h[words[val]] == 1:
            res = 2
            break
        else:
            if reversed in h:
                res += 2
    else:
        if reversed in h:
            res += 2


print(res)
