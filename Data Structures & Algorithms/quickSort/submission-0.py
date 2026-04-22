# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def sort(self,s,e,pairs):
        if e-s+1 <=1:
            return 
        pivot = pairs[e]
        left = s
        for i in range(s,e):
            if pairs[i].key<pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left+=1

        # swapping pivot at end
        
        pairs[e] = pairs[left]
        pairs[left] = pivot
       

        self.sort(s,left-1,pairs)
        self.sort(left+1,e,pairs) 

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        e = len(pairs)-1
        s = 0
        self.sort(s,e,pairs)
        return pairs


