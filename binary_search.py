# Given a sorted list and a target, this function will return the
# list index of the element if found.  Otherwise, it will return
# false.
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    found = False
    while start <= end and not found:

        mid = (end - start) // 2 + start
        if arr[mid] == target:
            found = True
            return mid
        else:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return found


arr = [1, 2, 5, 8, 30, 40]
print binary_search(arr, 30)