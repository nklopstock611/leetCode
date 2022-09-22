
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        h = {}
        l = []
        for i, num in enumerate(nums):
            if (target - num) not in h:
                h[num] = i
            else:
                l.append(h[(target - num)])
                l.append(i)
                
        
        return l


sol = Solution()
print(sol.twoSum([3, 3], 6))
