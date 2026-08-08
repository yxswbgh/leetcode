from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #⭐去重，想到哈希表
        #⭐原地改变数组/空间复杂度常数级，想到读指针，写指针

        #读指针元素与写指针元素比较，相同：read右移，不同：write右移并写入

        #类似于快慢指针，但前面几道题都是⭐满足条件，fast探路；不满足条件，slow右移直到满足条件
        #这里的双指针只是功能不同

        #为什么没用哈希表，因为不需要记忆功能


        read=0
        write=0

        while read<len(nums): #最后只会检查前write+1个，所以read可以跑到最后
            if (nums[read]==nums[write]): #相同就一直右移
                read+=1

            else: #不同：write右移并写入
                write+=1
                nums[write]=nums[read] 

        return write+1


