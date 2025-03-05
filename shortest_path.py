"""
**Shortest Path in a Maze**

Given a 2D grid representing a maze, find the shortest path from the start point to the endpoint.

**Example:**

Input:

```python
1 0 1 1 1  
1 1 1 0 1  
0 1 0 1 1  
1 1 1 1 1  
```

1 represents an open path, 0 represents a wall)

Output: Shortest path length = X (where X is the minimal number of steps required to reach the endpoint)
"""

import random


n_rows, n_cols = 4, 5  
n_states = n_rows * n_cols

env = [[1, 0, 1, 1, 1], 
       [1, 1, 1, 0, 1],  
       [0, 1, 0, 1, 1],  
       [1, 1, 1, 1, 1]]


states = [cell for row in env for cell in row]


actions = ['up', 'down', 'left', 'right']

episodes = []
total_episode = 1000

for _ in range(total_episode):
    curr_idx = 0 
    done = False
    step = 0
    while not done:
        action = random.choice(actions)

        if action == 'up' and curr_idx - n_cols >= 0 and states[curr_idx - n_cols] != 0:
            curr_idx -= n_cols
        elif action == 'down' and curr_idx + n_cols < n_states and states[curr_idx + n_cols] != 0:
            curr_idx += n_cols
        elif action == 'left' and curr_idx % n_cols > 0 and states[curr_idx - 1] != 0:
            curr_idx -= 1
        elif action == 'right' and curr_idx % n_cols < n_cols - 1 and states[curr_idx + 1] != 0:
            curr_idx += 1
        else:
            continue

        step += 1
        
        if curr_idx == n_states - 1:
            done = True
            episodes.append(step)



min_path = min(episodes)

print("Minimum number of steps to reach to the end is", min_path)


