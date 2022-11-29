# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def addTwoNumbersArray(self, a1, a2):
        sums = []
        saved = 0
        if len(a1) == len(a2):
            sums = self.calc(a1, a2, saved, sums)
        else:
            l2 = self.fill(a1, a2)
            sums = self.calc(a1, a2, saved, sums)

        return sums

    def printLinkedList(self, l, a):
        #print(l.val)
        a.append(l.val)
        if l.next != None:
            self.printLinkedList(l.next, a)
        
        return a

    def addTwoNumbers(self, l1, l2):
        a1 = []
        a2 = []
        self.printLinkedList(l1, a1)
        self.printLinkedList(l2, a2)
        l = self.addTwoNumbersArray(a1, a2)
        print(a1)
        print(a2)
        node = None
        for i in range(1, len(l)):
            val = l[i - 1]
            next = l[i]
            node = ListNode(val, next)
            print("NODE " + str(node.val))

s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, None)))
l2 = ListNode(1, ListNode(2, ListNode(3, None)))
s.addTwoNumbers(l1, l2)

            