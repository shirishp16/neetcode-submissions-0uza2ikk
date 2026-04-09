class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zeroCnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCnt += 1
            else:
                product = product * nums[i]
        
        for i in range(len(nums)):
            if zeroCnt > 1:
                output = [0] * len(nums)
                return output
            elif zeroCnt == 1 and nums[i] != 0:
                output.append(0)
            elif zeroCnt == 1 and nums[i] == 0:
                output.append(product)
            else:
                output.append(product // nums[i])
        
        return output
            


