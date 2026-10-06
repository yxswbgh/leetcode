class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #先排序再操作
        intervals.sort(key=lambda x:x[0]) #按区间左端点小到大

        cur=intervals[0]

        i=0
        res=[]
        while i+1<len(intervals): #next不能越位
            next=intervals[i+1]

            if cur[1]>=next[0]: #重叠
                cur[1]=max(cur[1],next[1])
            else:#不重叠，并入答案，并更新cur为next
                res.append(cur)
                cur=next
            i+=1
        res.append(cur) #加入最后一个不重叠的区间(因为else逻辑里是先append再更新，导致最后一个区间会漏)

        return res
