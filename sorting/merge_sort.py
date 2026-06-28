def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    # Test cases
    print(merge_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print(merge_sort([5, 1, 4, 2, 8]))                # [1, 2, 4, 5, 8]
    print(merge_sort([3, -1, -7, 0]))                 # [-7, -1, 0, 3]
    print(merge_sort([]))                             # []
    print(merge_sort([1]))                            # [1]
