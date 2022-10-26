import sys

def single(l: list) -> int:
    n = l[0]
    a = l[2]
    v = 0

    for i in range(n):
        v += a

    return v

def multiples(l: list) -> int:
    n = l[0]
    m = l[1]
    b = l[2]
    a = l[3]
    v = 0

    for i in range(m):
        v += a

    d = v

    for i in range(abs(n - v)):
        d += b

    return d

def solution(l: list) -> int:
    s = single(l)
    m = multiples(l)
    if s > m:
        return m
    else:
        return s


caso = sys.stdin.readline().strip(" \n").split(" ")
arreglo = []
n = len(caso)
for j in range(n):
    arreglo.append(int(caso[j]))

print(solution(arreglo))

