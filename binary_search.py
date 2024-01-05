def find_closest_element(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # At this point, left and right pointers have converged, and mid is the closest element
    def get_closest(arr, left, right):
        if left >= len(arr):
            return arr[right]
        if right < 0:
            return arr[left]
        if abs(arr[left] - target) < abs(arr[right] - target):
            return arr[left]
        else:
            return arr[right]

    return get_closest(arr, left, right)

sorted_array = [2, 3, 8]
target_value = 5
closest_element = find_closest_element(sorted_array, target_value)
print(f"The closest element to {target_value} is {closest_element}")
