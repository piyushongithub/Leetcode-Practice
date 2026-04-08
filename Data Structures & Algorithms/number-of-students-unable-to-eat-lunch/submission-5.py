class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {1:0,0:0}
        res = len(students)
        for s in students:
            count[s] = 1 + count.get(s,0)
        print(count)
        for s in sandwiches:
            if count[s]>0:
                res -= 1
                count[s]-=1
            else:
                return res
        return res
        


        