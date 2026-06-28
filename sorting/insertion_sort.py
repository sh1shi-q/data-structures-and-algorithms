def insertion_sort(arr: list[int]) -> list[int]:
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__ == "__main__":
    # Test cases
    print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print(insertion_sort([5, 1, 4, 2, 8]))                # [1, 2, 4, 5, 8]
    print(insertion_sort([3, -1, -7, 0]))                 # [-7, -1, 0, 3]
    print(insertion_sort([]))                             # []
    print(insertion_sort([1]))                            # [1]
