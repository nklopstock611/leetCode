class Solution:
    def findWinners(self, matches: list) -> list:
        d = {}
        ls = {}
        answer = []
        onlyW = []
        tookL = []

        for val in matches:
            if val[0] not in d:
                d[val[0]] = None
            if val[1] not in d:
                d[val[1]] = None

        for val in matches:
            if val[1] not in ls:
                ls[val[1]] = 1
            else:
                ls[val[1]] += 1

        for val in d:
            if val not in ls:
                onlyW.append(val)

        for val in ls:
            if ls[val] == 1:
                tookL.append(val)

        onlyW.sort()
        tookL.sort()

        answer.append(onlyW)
        answer.append(tookL)

        return answer

sol = Solution()
print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))