def selection_sort(arr: list[int]) -> list[int]:
    arr = arr.copy()  
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    # Test cases
    print(selection_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print(selection_sort([5, 1, 4, 2, 8]))                # [1, 2, 4, 5, 8]
    print(selection_sort([3, -1, -7, 0]))                 # [-7, -1, 0, 3]
    print(selection_sort([]))                             # []
    print(selection_sort([1]))                            # [1]