def merge_sort(arr):
    n = len(arr)
    curr_size = 1

    while curr_size < n:
        left = 0

        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)

            merge(arr, left, mid, right)
            left += 2 * curr_size

        curr_size *= 2

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_half = arr[left:left + n1]
    right_half = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(my_list)
print("Sorted array:", my_list)
