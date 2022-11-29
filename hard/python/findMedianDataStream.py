import math

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        middle = math.ceil(len(self.nums) / 2)
        median = 0
        if len(self.nums) % 2 == 0:
            median = ((self.nums)[middle - 1] + (self.nums)[middle]) / 2
        else:
            median = (self.nums)[middle - 1]

        return median

# obj = None
stream = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
nums = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
answer = []
i = 0
for data in stream:
    if data == "MedianFinder":
        obj = MedianFinder()
        answer.append(None)
    elif data == "addNum":
        num = nums[i][0]
        obj.addNum(num)
        answer.append(None)
    elif data == "findMedian":
        median = obj.findMedian()
        answer.append(median)

    i += 1

print(answer)


        