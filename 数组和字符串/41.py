class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i=0

        while i<len(nums): #不能用for，会自动i++
            num=nums[i]

            if num==i+1:
                i+=1
            else:
                if 1<=num<=len(nums) and num!=nums[num-1]: #有资格归位
                    temp=nums[num-1]
                    nums[num-1]=num
                    nums[i]=temp
                    
                    #nums[i],nums[num-1]=nums[num-1],nums[i] #交换两者
                else:
                    i+=1

        for i in range(len(nums)):
            if nums[i]==i+1:
                pass
            else:
                return i+1
        
        return len(nums)+1 #全体归位，返回长度+1