# Lists as Queues
from collections import deque

queue = deque([3, 4, 5])
queue.append(6)
queue.popleft()
queue.popleft()
print(queue)
