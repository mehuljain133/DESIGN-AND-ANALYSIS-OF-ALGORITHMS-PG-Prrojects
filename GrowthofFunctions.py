# Unit-I Review of Growth of Functions

import time
import math
import matplotlib.pyplot as plt
import numpy as np

# Define different time complexity functions
def constant(n):
    return 1

def logarithmic(n):
    return math.log(n) if n > 0 else 0

def linear(n):
    return n

def linearithmic(n):
    return n * math.log(n) if n > 0 else 0

def quadratic(n):
    return n ** 2

def cubic(n):
    return n ** 3

def exponential(n):
    return 2 ** n

# Compare growth of functions visually
def plot_growth():
    n_values = list(range(1, 20))
    functions = {
        "O(1)": [constant(n) for n in n_values],
        "O(log n)": [logarithmic(n) for n in n_values],
        "O(n)": [linear(n) for n in n_values],
        "O(n log n)": [linearithmic(n) for n in n_values],
        "O(n^2)": [quadratic(n) for n in n_values],
        "O(n^3)": [cubic(n) for n in n_values],
        "O(2^n)": [exponential(n) for n in n_values]
    }

    plt.figure(figsize=(12, 8))
    for label, values in functions.items():
        plt.plot(n_values, values, label=label)

    plt.yscale("log")  # Log scale to better compare growth
    plt.xlabel("Input size n")
    plt.ylabel("Time / Operations")
    plt.title("Growth of Common Functions")
    plt.legend()
    plt.grid(True)
    plt.show()

# Empirical time analysis
def empirical_analysis():
    def dummy_operation(n):
        total = 0
        for i in range(n):
            total += i
        return total

    sizes = [10**4, 10**5, 10**6]
    print("Empirical Time Complexity of dummy_operation(n):")
    for n in sizes:
        start = time.time()
        dummy_operation(n)
        end = time.time()
        print(f"n = {n:>7}, Time taken = {end - start:.6f} seconds")

# Big-O, Omega, Theta demonstrations (analytically)
def complexity_classes_demo():
    print("\nBig-O, Omega, Theta Demonstration:")
    print("f(n) = 3n + 2")
    print("Best-case: Ω(n)")
    print("Worst-case: O(n)")
    print("Tight bound: Θ(n)")

    print("\nf(n) = 5n^2 + 4n + 3")
    print("Best-case: Ω(n^2)")
    print("Worst-case: O(n^2)")
    print("Tight bound: Θ(n^2)")

# Main driver
def main():
    print("=== Design and Analysis of Algorithms: Unit I ===")
    plot_growth()
    empirical_analysis()
    complexity_classes_demo()

if __name__ == "__main__":
    main()
