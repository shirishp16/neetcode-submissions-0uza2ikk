class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            
            total += n

            if res < total:
                res = total

        return res
        