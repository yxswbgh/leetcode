from typing import List

class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #暴力解法：假设答案数组长度是1，...,n,遍历所有子数组
        for i in range(len(nums)): #长度为i
            for j in range(len(nums)):
                sums=sum(nums[j:j+i+1])
                if sums>=target:
                    return i+1 #i从0开始
        return 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #滑动窗口（快慢指针），申请两个指针，一个fast（探路） 一个slow
        #fast往右走，窗口变大，slow往左走，窗口变小
        #申请两个变量，sum，length（初始化为无穷大）
        #首先计算当前窗口的和，如果sum<target，fast右移（题目里都是正数）
        #fast一直移到sum>=target，看当前长度是否比length小，
        #如果是，更新length，然后slow右移，如果还满足sum>=target，更新length，⭐直到不满足条件，重新动fast
        #⭐最终就是fast到数组最后一个元素


        #⭐不满足条件：fast探路
        #⭐满足条件：slow找最短长度

        #⭐⭐⭐看到子数组，已经要想到滑动窗口了
        fast=0
        slow=0
        my_sum=0
        min_len=float('inf')

        while fast<len(nums):
            my_sum+=nums[fast] #第一次要记录窗口为1的第一个元素

            while my_sum>=target : #slow每右移一次就问是否还满足条件
                min_len=min(min_len,fast-slow+1) #更新答案，fast-slow+1=窗口长度，后面不用写min_len-=1,这边会一并更新
                #开始用slow试探
                my_sum-=nums[slow] #先减去再移动，如果先移动就是nums[slow-1]
                slow+=1

            #slow右移不满足条件了，fast右移
            fast+=1

        return min_len if min_len!=float('inf') else 0
               
        

    
        