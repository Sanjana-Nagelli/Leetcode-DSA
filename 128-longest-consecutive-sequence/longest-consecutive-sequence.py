class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        count=1
        ms=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                ms=max(ms,count)
            else:
                count=1
        return ms

        