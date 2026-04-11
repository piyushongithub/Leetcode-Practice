class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        sand = deque(sandwiches)
        stud = deque(students)
        while count<=len(stud)-1:
            if stud[0]==sand[0]:
                stud.popleft()
                sand.popleft()
                count=0
            else:
                ele = stud.popleft()
                stud.append(ele)
                count+=1
        return len(stud)
         


        