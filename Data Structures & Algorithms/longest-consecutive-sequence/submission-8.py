class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        
        for val in nums:
            if (val - 1) not in seen:
                curr = 1
                while (val + curr) in seen:
                    curr += 1
                if curr > longest:
                    longest = curr

        return longest
                
        


        