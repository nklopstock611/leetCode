
def compress(chars):
    ret = []
    aux = []
    count = 0
    actual = ''
    for i in range(0, len(chars)):
        actual = chars[i]
        if actual not in aux:
            if len(aux) == 0:
                aux.append(actual)
                ret.append(actual)
                count += 1
            else:
                ret.append(actual)
                count = 0
                aux.pop(0)
                aux.append(actual)
                count += 1
        else:
            ret.append(0)
            count += 1
            index = ret.index(actual)
            ret[index + 1] = str(count)

    # falta ajustar para el caso chars = ['a'] :: ['a'] y
    # el tema de que números mayores a 9 se deben representar como dos chars en diferentes posiciones de ret.

    return ret

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))