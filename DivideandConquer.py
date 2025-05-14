# Unit-III Divide and Conquer: Recurrence Relation, Master’s Theorem, Recursion Trees; Binary Search, Merge sort and Quick sort – time complexity and proof of correctness.

import time
import random
import math

# ======================
# Recurrence Helper (Master Theorem Application)
# ======================
def master_theorem(a, b, f_n):
    """
    Applies Master Theorem to T(n) = aT(n/b) + f(n)
    You must manually define f(n) as a lambda.
    """
    print(f"Master Theorem: T(n) = {a}T(n/{b}) + f(n)")
    print("Case analysis:")

    def log_b_a():
        return math.log(a, b)

    complexity_f = "n^" + str(round(log_b_a(), 2))
    print(f"log_b(a) = log_{b}({a}) = {log_b_a():.2f} -> Compare with f(n)")

    return f"Compare f(n) to n^{log_b_a():.2f} to determine the case."


# ======================
# Binary Search (Recursive)
# ======================
def binary_search(arr, target, left=0, right=None, depth=0):
    if right is None:
        right = len(arr) - 1
    print("  " * depth + f"Searching in {arr[left:right+1]}")

    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, left, mid - 1, depth + 1)
        else:
            return binary_search(arr, target, mid + 1, right, depth + 1)
    return -1

# ======================
# Merge Sort
# ======================
def merge_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr

    print("  " * depth + f"Dividing: {arr}")
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    print(f"Merging: {left} + {right}")
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

# ======================
# Quick Sort
# ======================
def quick_sort(arr, low=0, high=None, depth=0):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high, depth)
        quick_sort(arr, low, pivot_index - 1, depth + 1)
        quick_sort(arr, pivot_index + 1, high, depth + 1)
    return arr

def partition(arr, low, high, depth):
    pivot = arr[high]
    i = low - 1
    print("  " * depth + f"Partitioning: {arr[low:high+1]}, Pivot={pivot}")
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

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
# Proof of Correctness
# ======================
def test_correctness():
    print("\n=== Proof of Correctness ===")
    arr = [5, 3, 8, 4, 2]
    sorted_arr = sorted(arr)

    assert merge_sort(arr.copy()) == sorted_arr
    print("✅ Merge Sort passed")

    assert quick_sort(arr.copy()) == sorted_arr
    print("✅ Quick Sort passed")

    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 10) == -1
    print("✅ Binary Search passed")

# ======================
# Main Function
# ======================
def main():
    print("=== Unit-III: Divide and Conquer ===\n")

    # Recurrence Example
    print(">> Recurrence Example: T(n) = 2T(n/2) + n")
    print(master_theorem(2, 2, lambda n: n))
    print("→ Case 2: T(n) = Θ(n log n)\n")

    # Binary Search
    arr = list(range(1, 17))
    print(">> Binary Search Trace:")
    binary_search(arr, 9)

    # Merge Sort Trace
    print("\n>> Merge Sort Trace:")
    merge_sort([38, 27, 43, 3, 9, 82, 10])

    # Quick Sort Trace
    print("\n>> Quick Sort Trace:")
    quick_sort([38, 27, 43, 3, 9, 82, 10])

    # Time Benchmarking
    print("\n>> Timing (Random Dataset):")
    data = [random.randint(1, 100000) for _ in range(10000)]
    test_time(merge_sort, data.copy())
    test_time(quick_sort, data.copy())

    # Correctness Checks
    test_correctness()

if __name__ == "__main__":
    main()
