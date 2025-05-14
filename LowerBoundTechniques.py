# Unit-IV Lower bounding techniques: Decision Trees

import math
import itertools

# ======================
# Concept: Lower Bound using Decision Tree
# ======================

def sorting_lower_bound(n):
    """Calculate lower bound of comparison-based sorting using decision tree"""
    perms = math.factorial(n)
    height = math.ceil(math.log2(perms))
    print(f"\nFor sorting {n} elements:")
    print(f"Number of permutations: {perms}")
    print(f"Height of decision tree (min comparisons in worst case): ⌈log₂({perms})⌉ = {height}")
    print(f"⇒ Lower Bound: Ω(n log n)")

# ======================
# Decision Tree Printer (Toy Example)
# ======================

def print_decision_tree(elements, depth=0):
    """Print a textual decision tree (limited to small input for illustration)"""
    if len(elements) <= 1:
        print("  " * depth + f"Sorted: {elements}")
        return

    for i in range(len(elements) - 1):
        a, b = elements[i], elements[i + 1]
        print("  " * depth + f"Compare {a} and {b}:")
        less = elements.copy()
        less[i], less[i + 1] = min(a, b), max(a, b)
        print("  " * (depth + 1) + f"If {a} < {b} → {less}")
        print_decision_tree(less, depth + 2)

# ======================
# Brute Sort to Check All Permutations
# ======================

def generate_all_sorts(elements):
    """Simulate all permutations to mimic leaves of decision tree"""
    print(f"\nAll possible orderings (leaves of decision tree) for input: {elements}")
    for i, perm in enumerate(itertools.permutations(elements), 1):
        print(f"{i:>2}: {perm}")

# ======================
# Main Function
# ======================

def main():
    print("=== Unit-IV: Lower Bounding Techniques – Decision Trees ===")

    # Lower Bound Example
    sorting_lower_bound(4)  # Try with 3, 4, 5 for illustration

    # Print all leaves (sorted orders)
    generate_all_sorts([1, 2, 3])

    # Visual Decision Tree (limited to very small input due to branching)
    print("\nTextual Decision Tree (Partial, 3 Elements):")
    print_decision_tree([3, 1, 2])

if __name__ == "__main__":
    main()
