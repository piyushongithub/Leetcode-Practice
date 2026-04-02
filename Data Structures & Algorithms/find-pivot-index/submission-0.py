class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum=0
        for i in range(0,len(nums)):
            right_sum = total-(left_sum + nums[i]) # right side sum or post fix sum
            if right_sum==left_sum:
                return i
            left_sum+=nums[i] # prefix sum 
        return -1
        