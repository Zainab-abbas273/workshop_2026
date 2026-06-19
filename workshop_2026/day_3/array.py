# array is a data structure that stores a collection of elements, typically of the same type, in a contiguous block of memory.
#  It allows for efficient access and manipulation of its elements using indices. 
# Arrays can be one-dimensional (like a list) or multi-dimensional (like a matrix). 
# They are commonly used in programming for tasks such as storing data, implementing algorithms, and managing collections of items.



from pyparsing import nums


arr=[1, 2, 3, 4, 5]
print(arr)

# adding items to an array
arr.append(6)
print(arr)

# removing items from an array
arr.remove(3)
print(arr)

# reversing an array
arr.reverse()
print(arr)

# code for reversing an array using two pointers
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)

# code for reversing an array using slicing
arr = arr[::-1]
print(arr)

# code for reversing an array using size
size = len(arr)
for i in range(size // 2):
    arr[i], arr[size - 1 - i] = arr[size - 1 - i], arr[i]
print(arr)

# rotate an array to the right by k steps

n = len(arr)
k = 2

def reverse(left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse(0, n - 1)
reverse(0, k - 1)
reverse(k, n - 1)
print(arr)