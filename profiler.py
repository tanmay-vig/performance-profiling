import random
import time
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(100000)

# Sorting Algorithm Implementations

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Performance Profiler

def profile_algorithm(algorithm, data):
    tracemalloc.start()
    start_time = time.time()
    sorted_data = algorithm(data.copy())
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024  # time in seconds, memory in KB

# Dataset Sizes
sizes = [1000, 5000, 10000, 20000, 40000]
algorithms = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Bubble Sort": bubble_sort,
    "Timsort (sorted())": sorted
}

results_time = {alg: [] for alg in algorithms}
results_memory = {alg: [] for alg in algorithms}

# Run Profiling
for size in sizes:
    print(f"\nProfiling with dataset size: {size}")
    base_data = random.sample(range(0, size * 2), size)
    for name, func in algorithms.items():
        if name == "Bubble Sort" and size > 5000:
            results_time[name].append(None)
            results_memory[name].append(None)
            continue
        print(f"  Running {name}...")
        exec_time, mem = profile_algorithm(func, base_data)
        results_time[name].append(exec_time)
        results_memory[name].append(mem)

# Plotting
def plot_results(results, ylabel, title):
    for name, values in results.items():
        sizes_filtered = [sizes[i] for i in range(len(values)) if values[i] is not None]
        values_filtered = [v for v in values if v is not None]
        plt.plot(sizes_filtered, values_filtered, label=name)
    plt.xlabel("Input Size")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_results(results_time, "Execution Time (seconds)", "Sorting Algorithm Time Complexity")
plot_results(results_memory, "Memory Usage (KB)", "Sorting Algorithm Memory Usage")
