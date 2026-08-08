from typing import List

class Solution1:
    #自己想的
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0] *n
        detail=[[0]*n for _ in range(len(bookings))] #每个记录具体到航班的座位数
        for i in range(len(bookings)):
            for j in range(bookings[i][0],bookings[i][1]+1):
                detail[i][j-1]=bookings[i][2] #记录座位数,j-1要把航班-->下标

        ans=[sum(col) for col in zip(*detail)]

        return ans


class Solution2:
    #视频法一，暴力法O(mn)
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer=[0]*n

        for first,last,seats in bookings:
            for i in range(first-1,last): #-1是因为要把航班-->下标，last不用减1因为本身就是开区间
                answer[i]+=seats

        return answer


        
