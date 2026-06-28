def quick_sort(arr: list[int], low = 0, high = None) -> list[int]:
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr

def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":  
    # Test cases
    print(quick_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print(quick_sort([5, 1, 4, 2, 8]))                # [1, 2, 4, 5, 8]
    print(quick_sort([3, -1, -7, 0]))                 # [-7, -1, 0, 3]
    print(quick_sort([]))                             # []
    print(quick_sort([1]))                            # [1]