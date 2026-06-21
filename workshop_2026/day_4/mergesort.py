def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
arr = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(arr))