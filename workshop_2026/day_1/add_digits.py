# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         return 1 + (num - 1) % 9

def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

num = int(input("Enter a number: "))
print(addDigits(num))