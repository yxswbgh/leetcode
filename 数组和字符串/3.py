class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #跟209很像，只不过条件变成元素不重复的最长字串
        #⭐看到重复，想到集合：元素不重复
        #⭐同时看到子数组（子串），直接想到滑动窗口

        #右指针探路，找到满足条件的窗口
        #一旦不满足动左指针，直到满足条件
        l=0
        r=0
        max_len=0 
        my_set=set() #记录满足条件下当前窗口的元素

        while r<len(s):
            if s[r] in my_set: #记录过（重复）
                my_set.remove(s[l])
                l+=1
 
            else: #当前元素没记录过
                my_set.add(s[r]) 
                max_len=max(max_len,len(my_set))
                r+=1
        return max_len

            
