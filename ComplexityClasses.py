# Unit-XI Introduction to Complexity Classes: P, NP, NP-Hard, NP-Complete.

from itertools import combinations, permutations

# ===============================
# 1. P Class Example: Binary Search
# ===============================
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# ===============================
# 2. NP Class Example: Subset Sum
# ===============================
def subset_sum(nums, target):
    n = len(nums)
    for r in range(1, n+1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                return True
    return False

# ===============================
# 3. NP-Complete (Simplified): 3-SAT
# ===============================

def is_clause_satisfied(clause, assignment):
    for var in clause:
        if var.startswith('~'):
            if not assignment.get(var[1:], False):
                return True
        else:
            if assignment.get(var, False):
                return True
    return False

def is_3sat_satisfied(clauses, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in clauses)

def brute_force_3sat(clauses, variables):
    from itertools import product
    for bits in product([False, True], repeat=len(variables)):
        assignment = dict(zip(variables, bits))
        if is_3sat_satisfied(clauses, assignment):
            return True
    return False

# ===============================
# 4. NP-Hard (Heuristic): TSP (Traveling Salesman Problem)
# ===============================
def tsp_brute_force(graph):
    n = len(graph)
    min_cost = float('inf')
    best_path = []

    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        cost = sum(graph[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return min_cost, best_path

# ===============================
# Test All
# ===============================
def test_all():
    print("=== Unit-XI: Complexity Classes ===\n")

    # P Class
    print("P Class (Binary Search):")
    arr = [1, 2, 3, 4, 5, 6]
    print(f"Search 4: {binary_search(arr, 4)}")
    print(f"Search 9: {binary_search(arr, 9)}\n")

    # NP Class
    print("NP Class (Subset Sum):")
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"Subset sum to {target}: {subset_sum(nums, target)}\n")

    # NP-Complete
    print("NP-Complete (Brute-force 3-SAT):")
    variables = ['x1', 'x2', 'x3']
    clauses = [['x1', '~x2', 'x3'], ['~x1', 'x2', '~x3']]
    print(f"3-SAT satisfiable: {brute_force_3sat(clauses, variables)}\n")

    # NP-Hard
    print("NP-Hard (TSP Brute Force):")
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    cost, path = tsp_brute_force(graph)
    print(f"Min TSP Cost: {cost}")
    print(f"Path: {path}")

if __name__ == "__main__":
    test_all()
