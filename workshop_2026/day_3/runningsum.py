# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         return nums

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

result = runningSum([1, 2, 3, 4])
print(result)
