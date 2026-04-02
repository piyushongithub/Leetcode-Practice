class Solution:
   def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this is with prefix and postfix array O(2n) space complexity
        prefix_arr = [1]*len(nums)
        suffix_arr = [1]*len(nums)
        prefix_product=1
        for i in range(len(nums)):
            prefix_product=prefix_product*nums[i]
            prefix_arr[i]=prefix_product
        
        suffix_product=1
        for i in range(len(nums)-1,-1,-1):
            suffix_product=suffix_product*nums[i]
            suffix_arr[i]=suffix_product
        
        for i in range(len(nums)):
            if i==0 :
                nums[i]=1*suffix_arr[i+1]
            elif i==len(nums)-1:
                nums[i]=prefix_arr[i-1]*1
            else:
                nums[i]=prefix_arr[i-1]*suffix_arr[i+1]


        return nums
        