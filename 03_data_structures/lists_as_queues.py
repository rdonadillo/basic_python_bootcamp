# Lists as Queues

# Create a sample "First-In, First-Out"
# We can use deque library
from collections import deque

queue = deque([3, 4, 5])
queue.append(6)
queue.popleft()
queue.popleft()
print(queue)
