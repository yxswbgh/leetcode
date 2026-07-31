from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #暴力
        for i,item in enumerate(nums):
            for  j in range(i+1,len(nums)):
                post=nums[j]
                if item+post==target:
                    return [i,j]


class Solution2:
    #哈希表（记忆功能，本题记住每个元素的下标）
    #暴力解法在第二层循环会重复遍历相同元素
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={} #key需要唯一
        for i,item in enumerate(nums):
            cache[item]=i

        for i,item in enumerate(nums):
            other=target-item
            if other in cache and cache[other]!=i: #不能用两次相同的元素记录答案，例如[0,0]，and后面排除类似情况
                return [i,cache[other]]


class Solution3:
    #不遍历两遍
    #遍历到当前元素时，跟之前遍历过（在哈希表里）的元素对比，同时将当前元素记录进哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):#记录和判断放在同一个循环里
            other=target-item
            if other in cache:
                return [i,cache[other]]
            cache[item]=i