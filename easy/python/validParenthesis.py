s = "()[]"

c = 0
for val in s:
    if val == "(":
        c += 1
    elif val == "[":
        c += 2
    elif val == "{":
        c += 3
    elif val == ")":
        c -= 1
    elif val == "]":
        c -= 2
    elif val == "}":
        c -= 3

res = False
if c == 0:
    res = True

print(res)

