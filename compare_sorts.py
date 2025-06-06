import time
import random
from heapsort import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def run_benchmark():
    sizes = [1000, 5000, 10000]
    print("Size | Heap     | Quick    | Merge")
    print("-------------------------------------")
    for size in sizes:
        data = random.sample(range(size * 10), size)

        for name, func in [("Heap", heapsort), ("Quick", quicksort), ("Merge", mergesort)]:
            copy = data.copy()
            start = time.time()
            func(copy)
            duration = time.time() - start
            print(f"{size:<5} | {duration:.5f}", end="   ")
        print()

if __name__ == "__main__":
    run_benchmark()
