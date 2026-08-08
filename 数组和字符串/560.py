from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #⭐⭐⭐这道题不能用快慢指针，因为209可以用是因为nums全正/全负，fast右移数字一定变大，slow右移数字一定变小
        #⭐fast和slow的移动一定会导致窗口会更加靠近/远离条件
        #但是这个题只说整数数组，没说符号相同，因此fast和slow的移动与总和大小的变化无关，所以做不了

        #⭐看到子数组和--->前缀和令为P
        #则此题转化为找P子数组使得P[j+1]-P[i]=k -->两数之差-->哈希表
        count=0
        p=[0]*(len(nums)+1)

        for i in range(len(nums)):
            p[i+1]=p[i]+nums[i]

        cache={} #item出现了几次，⭐出现过几次答案就多几种，因为前缀和数组p不单调，题1是因为每种输入只会对应一个答案
        for i,item in enumerate(p):
            
            other=item-k #other是以前遍历过的，排在左边

            if  other in cache:
                count+=cache[other] #other可能出现过好几次，⭐出现过几次答案就多几种

            cache[item]=cache.get(item,0)+1 #如果有item字段的值get出来，没有返回0，+1是因为再加一次出现次数

        return count
