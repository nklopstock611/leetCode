s = "abBAcC"
l = []
for val in s:
    l.append(val)

n = len(l)
for i in range(1, n):
        print(i)
        print(l)
        print(len(l))
        if i != 0 and i < len(l) and l[i].upper() == l[i - 1]:
            act = l[i]
            ant = l[i - 1]
            l.remove(act)
            l.remove(ant)
        elif i < len(l) - 1 and l[i].upper() == l[i + 1]:
            print("desp")
            act = l[i]
            sig = l[i + 1]
            l.remove(act)
            l.remove(sig)
        elif i >= len(l):
            break

c = ''
for i in l:
    c += val

print(c)                    
    