class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for val in nums:
            if val not in seen:
                seen.add(val)
        
        sort = sorted(seen)
        curr, longest = 0, 0
        if len(nums) > 0:
            curr, longest = 1, 1
        
        prev = None
        for val in sort:
            if (val - 1) == prev:
                curr += 1
            else:
                curr = 1
            if curr > longest:
                longest = curr
            prev = val
        
        return longest
        


        