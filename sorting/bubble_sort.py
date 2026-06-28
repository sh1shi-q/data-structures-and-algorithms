def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    # Test cases
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print(bubble_sort([5, 1, 4, 2, 8]))                # [1, 2, 4, 5, 8]
    print(bubble_sort([3, -1, -7, 0]))                 # [-7, -1, 0, 3]
    print(bubble_sort([]))                             # []
    print(bubble_sort([1]))                            # [1]