def indices(l, wordrep):
    ini = None
    fini = None
    for i in range(len(l)):
        if l[i] == '[':
            ini = i + 1
            break
    i = len(l) - 1
    for val in reversed(wordrep):
        if val == ']':
            fini = i
            break
    i -= 1

    word = l[ini:fini]
    return (ini, fini, word)

def decode(l, wordrep):
    ns = ['1', '2', '3']
    ini = indices(l, wordrep)[0]
    fini = indices(l, wordrep)[1]
    wordrep = indices(l, wordrep)[2]

    if ini != None and fini != None:
        return decode(l, wordrep)
    else:
        return 0


print(decode('3[abc2[bc]]', '3[abc2[bc]]'))