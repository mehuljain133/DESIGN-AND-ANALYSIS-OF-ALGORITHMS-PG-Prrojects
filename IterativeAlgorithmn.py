# Unit-II Iterative Algorithms: Searching and Sorting Techniques - Linear search, Binary search, insertion sort – time complexity and proof of correctness

import time
import random

# ======================
# Linear Search
# ======================
def linear_search(arr, target):
    """Iterative Linear Search"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ======================
# Binary Search
# ======================
def binary_search(arr, target):
    """Iterative Binary Search - assumes sorted array"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ======================
# Insertion Sort
# ======================
def insertion_sort(arr):
    """Iterative Insertion Sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ======================
# Time Complexity Tester
# ======================
def test_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__} executed in {(end - start):.6f}s")
    return result

# ======================
# Proof of Correctness (Assertions)
# ======================
def test_correctness():
    print("\n=== Proof of Correctness (Assertions) ===")

    # Insertion sort correctness
    original = [5, 2, 9, 1, 5, 6]
    sorted_copy = sorted(original)
    assert insertion_sort(original.copy()) == sorted_copy
    print("Insertion Sort passed ✅")

    # Linear search correctness
    data = [10, 20, 30, 40, 50]
    for idx, val in enumerate(data):
        assert linear_search(data, val) == idx
    assert linear_search(data, 100) == -1
    print("Linear Search passed ✅")

    # Binary search correctness
    sorted_data = [1, 3, 5, 7, 9, 11]
    for idx, val in enumerate(sorted_data):
        assert binary_search(sorted_data, val) == idx
    assert binary_search(sorted_data, 4) == -1
    print("Binary Search passed ✅")

# ======================
# Main Function
# ======================
def main():
    print("=== Unit-II: Iterative Algorithms ===")
    size = 10000
    arr = [random.randint(1, 100000) for _ in range(size)]
    target = arr[size // 2]

    # Linear Search Time
    test_time(linear_search, arr, target)

    # Insertion Sort Time
    small_arr = arr[:1000]
    test_time(insertion_sort, small_arr.copy())

    # Binary Search (requires sorted)
    sorted_arr = sorted(arr)
    test_time(binary_search, sorted_arr, target)

    test_correctness()

if __name__ == "__main__":
    main()
