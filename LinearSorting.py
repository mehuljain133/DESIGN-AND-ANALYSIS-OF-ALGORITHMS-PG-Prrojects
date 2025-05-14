# Unit-V Linear Sorting: Count Sort, Radix Sort, Bucket Sort.

import time
import random
from collections import defaultdict

# ======================
# Counting Sort
# ======================
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1

    index = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[index] = i
            index += 1
    return arr

# ======================
# Radix Sort (LSD)
# ======================
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
    return arr

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

# ======================
# Bucket Sort
# ======================
def bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)

    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Using built-in sort for small buckets

    return sorted_arr

# ======================
# Timing Utility
# ======================
def test_time(func, arr):
    start = time.time()
    result = func(arr.copy())
    end = time.time()
    print(f"{func.__name__} executed in {(end - start):.6f}s")
    return result

# ======================
# Proof of Correctness
# ======================
def test_correctness():
    print("\n=== Proof of Correctness ===")
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1],
        [170, 45, 75, 90, 802, 24, 2, 66],
        [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    ]

    # Convert float array to int (0-99) for bucket sort test
    float_to_int = [int(x * 100) for x in test_arrays[2]]

    assert counting_sort(test_arrays[0].copy()) == sorted(test_arrays[0])
    print("✅ Counting Sort passed")

    assert radix_sort(test_arrays[1].copy()) == sorted(test_arrays[1])
    print("✅ Radix Sort passed")

    assert bucket_sort(float_to_int.copy()) == sorted(float_to_int)
    print("✅ Bucket Sort passed")

# ======================
# Main Function
# ======================
def main():
    print("=== Unit-V: Linear Sorting Algorithms ===\n")

    size = 10000
    arr = [random.randint(0, 9999) for _ in range(size)]

    print(">> Timing on Random Integers:")
    test_time(counting_sort, arr)
    test_time(radix_sort, arr)
    test_time(bucket_sort, arr)

    test_correctness()

if __name__ == "__main__":
    main()
