def search(nums, target):
    return binary_search(nums, 0, len(nums)-1, target)


def binary_search(nums, left, right, target):
    mid = left + (right - left) / 2

    # Stop if mid is equal to target.
    if nums[mid] == target:
        return mid

    # If mid is less than or equal to the rightmost element, the right segment is strictly ordered.
    # Then, let's search there. If not, search the left segment.
    if nums[mid + 1] <= nums[right]:
        if nums[mid + 1] <= target <= nums[right]:
            return binary_search(nums, mid + 1, right, target)
        else:
            return binary_search(nums, left, mid - 1, target)
    # If mid is greater than or equal to the leftmost element, the left segment is strictly ordered.
    # Then, let's search there. If not, search the right segment.
    elif nums[left] <= nums[mid]:
        if nums[left] <= target <= nums[mid - 1]:
            return binary_search(nums, left, mid - 1, target)
        else:
            return binary_search(nums, mid + 1, right, target)

nums = [4, 7, 8, 2, 3]

print search(nums, 3)