class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        curr = 2 # n wasys to reach 2nd step from 0
        prev = 1 # n wasys to reach 1st step from 0

        # using fibonacci like pattern
        for i in range(3,n+1):
            temp = curr
            curr = curr+prev 
            prev = temp
        return curr
        