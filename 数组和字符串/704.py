from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #⭐有序，找到某个元素--->二分查找 O(logN)(以2为底)
        #⭐记住左闭右开
        l=0
        r=len(nums) #指向最后一个元素往右一个位置
        #因为要在[l,r)这个区间去找，所以要往右1个位置

        mid=(l+r)//2

        while l<r: #条件：left==right ，相当于一个区间就一个数，[)，既能取又不能取
            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                l=mid+1

            else:
                r=mid #因为是左闭右开，所以不用-1

            mid=(l+r)//2

        return -1
