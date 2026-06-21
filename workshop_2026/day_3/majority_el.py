class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        app=n//2
        h={}
        for i in range(n):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
            if app<h[nums[i]]:
                return nums[i]
nums=[2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
