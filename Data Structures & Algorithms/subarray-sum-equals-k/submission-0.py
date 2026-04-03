class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hashmap = {}
        count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum==k:
                count+=1
            if prefix_sum-k in hashmap:
                count+=hashmap[prefix_sum-k]
            hashmap[prefix_sum]= 1 + hashmap.get(prefix_sum,0)
        return count
        