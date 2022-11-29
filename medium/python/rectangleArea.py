ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2

ax = set()
bx = set()

ay = set()
by = set()

for i in range(ax1, ax2 + 1):
    ax.add(i)

for i in range(bx1, bx2 + 1):
    bx.add(i)

for i in range(ay1, ay2 + 1):
    ay.add(i)

for i in range(by1, by2 + 1):
    by.add(i)

b = list(ax.intersection(bx))[-1]
h = list(ay.intersection(by))[-1]

aa = (abs(ax1) + abs(ax2)) * (abs(ay1) + abs(ay2))
ab = (abs(bx1) + abs(bx2)) * (abs(by1) + abs(by2))

res = (aa + ab) - (h * b)

print(res)


