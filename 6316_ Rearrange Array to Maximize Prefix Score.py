class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        res = 0
        ans = 0
        for i in range(0, len(nums)):
            res += nums[i]
            if (res > 0):
                ans += 1
            else:
                break
            
                
        return ans