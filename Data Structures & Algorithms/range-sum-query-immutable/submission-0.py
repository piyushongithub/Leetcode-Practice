class NumArray:

    def __init__(self, nums: List[int]):
        self.numsarr = nums

        for i in range(1,len(self.numsarr)):
            self.numsarr[i]+=self.numsarr[i-1]
        print(self.numsarr)

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.numsarr[left-1] if left>0 else 0
        return self.numsarr[right] - leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)