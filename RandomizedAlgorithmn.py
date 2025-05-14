# Unit-X Randomized algorithms: Introduction to random numbers, randomized Qsort, randomly built BST

import random

# ========================================
# 1. Random Numbers in Python
# ========================================

def generate_random_numbers(count, lower, upper):
    return [random.randint(lower, upper) for _ in range(count)]

# ========================================
# 2. Randomized QuickSort
# ========================================

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# ========================================
# 3. Randomly Built Binary Search Tree
# ========================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_bst(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

def inorder_bst(root):
    if root:
        inorder_bst(root.left)
        print(root.key, end=' ')
        inorder_bst(root.right)

def build_random_bst(elements):
    random.shuffle(elements)
    root = None
    for key in elements:
        root = insert_bst(root, key)
    return root

# ===============================
# Run All Examples
# ===============================

def test_all():
    print("=== Unit-X: Randomized Algorithms ===\n")

    # 1. Random Numbers
    print("Random Numbers (5 between 1 and 10):")
    print(generate_random_numbers(5, 1, 10))

    # 2. Randomized QuickSort
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("\nOriginal Array for Randomized QuickSort:")
    print(arr)
    randomized_quicksort(arr, 0, len(arr) - 1)
    print("Sorted Array:")
    print(arr)

    # 3. Random BST
    elements = [50, 30, 70, 20, 40, 60, 80]
    print("\nRandomized BST (inorder traversal):")
    bst_root = build_random_bst(elements[:])  # copy to avoid modifying original
    inorder_bst(bst_root)
    print()

if __name__ == "__main__":
    test_all()
