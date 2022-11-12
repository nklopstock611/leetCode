s = "aaaaaaaa" # revisar este caso, porque no vuelve a revisar el comienzo
l = []
for val in s:
    l.append(val)

n = len(l)
i = 1
centinela = True
while i < n and centinela:
    if len(l) == 0:
        centinela = False
    elif i < 0:
        i = i * -1
    else:
        if i != 0 and i < len(l) and l[i] == l[i - 1]:
            act = l[i]
            ant = l[i - 1]
            l.pop(i)
            l.pop(i - 1)
            i -= 2
        elif i < len(l) - 1 and l[i] == l[i + 1]:
            act = l[i]
            sig = l[i + 1]
            l.pop(i)
            l.pop(i)
            i -= 2

    i += 1

c = ''
for val in l:
    c += val

print(c)