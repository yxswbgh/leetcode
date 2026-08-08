from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        #⭐前缀和：第i个位置储存前i个元素的和
        #⭐因此有len(nums)+1个元素,presum[0]=0,presum[len(nums)]=sum(nums) #从第0个元素到第n个元素
        #则nums[i]+...nums[j]=presum[j+1]-presum[i]=(nums[0]+...nums[j])-(nums[0]+...nums[i-1])
        #算出前缀和T(n)=O(n),但是算任意区间和O(1)
        #⭐对数组某个区间有大量求和（平均）操作，想到前缀和
        self.preSum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.preSum[i+1]=self.preSum[i]+nums[i] #当前元素加上前面的前缀和,presum[0]=0不用算

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1]-self.preSum[left]