class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = []
        n = len(temperatures)
        res = [0] * n
        # print(res)
        for i in range(0,n):
            t = temperatures[i]
            while (len(lst) != 0) and (temperatures[lst[-1]] < t):
                lessIndex = lst.pop()
                res[lessIndex] = i - lessIndex
            lst.append(i)
        return res