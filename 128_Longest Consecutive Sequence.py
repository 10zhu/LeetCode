class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        lst = []
        for i in nums:
            dic[i] = 1
        for i in range(0, len(nums)):
            if nums[i] - 1 not in dic:
                lst.append(nums[i])
                # res += 1
        for i in range(0, len(lst)):
            tmp = 1
            j = lst[i] + 1
            while (j > lst[i]):
                if j in dic:
                    tmp += 1
                    j += 1
                elif j not in dic:
                    break
            res = max(res, tmp)

        return res


