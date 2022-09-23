
class Solution:

    def calc(self, l1, l2, saved, sums):
        for i in range(len(l1)):
            sum = l1[i] + l2[i] + saved
            if sum >= 10:
                sum -= 10
                sums.append(sum)
                saved = 1
            else:
                sums.append(sum)
        return sums

    def fill(self, l1, l2):
        length = len(l1) > len(l2)
        i = 0
        if length:
            while i < (len(l1) - len(l2)):
                l2.append(0)
                i += 1
            return l2
        else:
            while i < (len(l2) - len(l1)):
                l1.append(0)
                i += 1
            return l1

    def addTwoNumbers(self, l1: list, l2: list) -> list:
        sums = []
        saved = 0
        if len(l1) == len(l2):
            sums = self.calc(l1, l2, saved, sums)
        else:
            l2 = self.fill(l1, l2)
            sums = self.calc(l1, l2, saved, sums)

        return sums

sol = Solution()
l1 = [2, 6, 3, 9]
l2 = [5, 6, 4]
print(sol.addTwoNumbers(l1, l2))
