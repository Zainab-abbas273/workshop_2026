# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i in range(len(nums)):
#             comp = target - nums[i]
#             if comp in d:
#                 return [d[comp], i]
#             d[nums[i]] = i

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in d:
            return [d[comp], i]
        d[nums[i]] = i

two_sum_result = twoSum([2, 7, 11, 15], 9)
print(two_sum_result)