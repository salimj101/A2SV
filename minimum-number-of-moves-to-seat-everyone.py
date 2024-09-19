class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        val=[]

        for i in range(len(seats)):
            val.append(abs(seats[i]-students[i]))
        return sum(val)