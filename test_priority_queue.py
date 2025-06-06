from priority_queue import Task, PriorityQueue

pq = PriorityQueue()

pq.insert(Task("A", priority=3, arrival_time=1))
pq.insert(Task("B", priority=1, arrival_time=2))
pq.insert(Task("C", priority=5, arrival_time=3))

print("Initial queue:")
for task in pq.heap:
    print(task)

print("\nExtracted task:")
print(pq.extract_min())

print("\nQueue after extraction:")
for task in pq.heap:
    print(task)

pq.decrease_key("C", 0)

print("\nQueue after decreasing priority of Task C:")
for task in pq.heap:
    print(task)

print("\nIs queue empty?")
print(pq.is_empty())
