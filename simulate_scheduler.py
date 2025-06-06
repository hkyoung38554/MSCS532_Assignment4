from priority_queue import Task, PriorityQueue

# Simulated current time
current_time = 0

# Sample tasks with different priorities and arrival times
tasks = [
    Task("Task1", priority=4, arrival_time=0, deadline=10),
    Task("Task2", priority=2, arrival_time=1, deadline=8),
    Task("Task3", priority=1, arrival_time=2, deadline=6),
    Task("Task4", priority=3, arrival_time=3, deadline=9),
    Task("Task5", priority=5, arrival_time=4, deadline=12),
]

pq = PriorityQueue()

print("Starting task scheduling simulation...\n")

# Simulate time from 0 to 10
for current_time in range(0, 10):
    # Insert tasks that arrive at this time
    for task in tasks:
        if task.arrival_time == current_time:
            pq.insert(task)
            print(f"Time {current_time}: Inserted {task}")

    # Simulate executing a task at each time step
    if not pq.is_empty():
        task = pq.extract_min()
        print(f"Time {current_time}: Executed {task}")

print("\nSimulation completed.")
