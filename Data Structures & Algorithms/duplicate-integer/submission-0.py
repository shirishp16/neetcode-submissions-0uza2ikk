class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        isDup = False
        for i in nums:
            if i in seen:
                isDup = True
            else:
                seen.add(i)
        return isDup
        