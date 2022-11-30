import random

class RandomizedSet:

    def __init__(self):
        self.d = {}        

    def insert(self, val: int) -> bool:
        b = False
        if val not in self.d:
            (self.d)[val] = None
            b = True
        
        return b

    def remove(self, val: int) -> bool:
        b = False
        if val in self.d:
            (self.d).pop(val)
            b = True

        return b        

    def getRandom(self) -> int:
        randInt = random.randint(0, len(self.d) - 1)
        l = list((self.d).keys())
        randValue = l[randInt]
        return randValue

# Your RandomizedSet object will be instantiated and called as such:
ins = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
vals = [[], [1], [2], [2], [], [1], [2], []]
answer = []
obj = None
for i, val in enumerate(ins):
    if val == "RandomizedSet":
        obj = RandomizedSet()
        answer.append(None)
    elif val == "insert":
        answer.append(obj.insert(vals[i][0]))
    elif val == "remove":
        answer.append(obj.remove(vals[i][0]))
    elif val == "getRandom":
        answer.append(obj.getRandom())

print(answer)
