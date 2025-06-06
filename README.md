# MSCS532 Assignment4: Heap Data Structures – Implementation, Analysis, and Applications

This project implements and analyzes Heapsort and a Priority Queue using binary heaps. It includes time and space complexity analysis, empirical comparisons with other sorting algorithms, and a real-world task scheduling simulation using the priority queue.

## Files

- `heapsort.py`: Python implementation of Heapsort using a max-heap
- `compare_sorts.py`: Benchmark script comparing Heapsort with Quicksort and Merge Sort
- `priority_queue.py`: Priority Queue implementation using a min-heap and Task class
- `test_priority_queue.py`: Test script demonstrating core priority queue operations
- `simulate_scheduler.py`: Task scheduling simulation using the implemented priority queue
- `report.md`: Report draft in markdown format
- `Assignment4_Haeri Kyoung.pdf`: Final written report containing implementation, analysis, simulation, and results
- `README.md`: Instructions and summary of the project

## How to Run

```bash
python compare_sorts.py
python test_priority_queue.py
python simulate_scheduler.py
```

## Summary of Findings

### Heapsort

- Performed consistently with time complexity of order n log n in best, average, and worst cases.
- Used no additional memory beyond the input array, operating fully in place.
- Slightly slower than Quicksort in practice due to overhead but offered stable performance and predictable behavior.
- Outperformed Merge Sort in memory efficiency and avoided worst-case degradation seen in Quicksort.

### Priority Queue

- Implemented with a binary min-heap to always return the task with the lowest numerical priority.
- Core operations including insert, extract_min, decrease_key, and is_empty all performed as expected in logarithmic or constant time.
- Demonstrated correctness and efficiency through test script and printed output.

### Task Scheduling Simulation

- Simulated arrival and execution of tasks based on priority and arrival time.
- Verified that the queue always selected the most urgent task regardless of when it arrived.
- Reflected real-world behavior seen in CPU scheduling or event handling systems.

---

This assignment strengthened my understanding of heap-based sorting and priority queues while reinforcing the value of efficient task scheduling strategies.
