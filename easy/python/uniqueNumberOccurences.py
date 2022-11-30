class Solution:

    def areThereReps(self, arr: list) -> bool:
        h = {}
        b = True
        for each_num in arr:
            if each_num not in h:
                h[each_num] = None
            else:
                b = False
        
        return b

    def uniqueOccurrences(self, arr: list) -> bool:
        d = {}
        for each_num in arr:
            if each_num not in d:
                d[each_num] = 1
            else:
                d[each_num] += 1

        values = list(d.values())
        answer = self.areThereReps(values)
        return answer

sol = Solution()
arr = [1,2,2,1,1,3]
print(sol.uniqueOccurrences(arr))