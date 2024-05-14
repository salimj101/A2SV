def count_elements_less_than(arr1, arr2):
    result = []
    for num in arr2:
        left = 0
        right = len(arr1) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr1[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        result.append(left)
    return result

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*count_elements_less_than(arr1, arr2))
