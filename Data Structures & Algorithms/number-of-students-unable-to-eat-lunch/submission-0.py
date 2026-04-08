class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        size = len(students)
        sand = deque(sandwiches)
        stud = deque(students)
        while count<size:
            if stud[0]==sand[0]:
                stud.popleft()
                sand.popleft()
                count=0
                size-=1
            else:
                ele = stud.popleft()
                stud.append(ele)
                count+=1
            print(size)
        return size
        