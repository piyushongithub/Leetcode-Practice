class Solution:
   def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this is with one output array array O(n) space complexity
        output = [1]*len(nums)
        prefix = 1
        postfix=1
        # forward pass
        for i in range(len(nums)):
            output[i]=prefix
            prefix*=nums[i]
        
        # backward pass
        for i in range(len(nums)-1,-1,-1):
            output[i] *=postfix 
            postfix*=nums[i]

        return output
        