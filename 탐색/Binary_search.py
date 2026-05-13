def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      high = mid - 1
    else:
      low = mid + 1
  return - 1

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_value = 70

result = binary_search(data, target_value)
print(f"위치: {result}")