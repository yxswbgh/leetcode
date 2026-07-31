from typing import List
#你所设计的解决方案必须只使用常量级的额外空间
class Solution1:
    #题目1稍稍修改，但是没有用常量级额外空间
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #⭐哈希表是牺牲空间换时间
        cache={} #不能申请一长串数组，空间复杂度=O(n)，不符合题意
        for i,item in enumerate(numbers):
            other=target-item
            if other in cache:
                return [cache[other]+1,i+1] #当前下标肯定是大的，因为哈希表里的元素已经遍历过
                #return [i+1,cache[other]+1] if (i+1)<(cache[other]+1) else [cache[other]+1,i+1]
            cache[item]=i


class Solution2:
    #⭐因为是递增数组，双指针
    #左右指针，如果和>target，右指针左移
    #         如果和<target,左指针右移
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while not(left==right): #⭐左=右的时候跳出，所以取反就是while条件
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum>target:
                right-=1
            elif sum<target:
                left+=1