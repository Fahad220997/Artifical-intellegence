

1. Compare the solution paths found by BFS, DFS, and A*

BFS Solution Path

(0, 0) → (4, 0) → (1, 3)

DFS Solution Path

(0, 0) → (0, 3) → (3, 0) → (3, 3) → (4, 2) → (4, 0) → (1, 3)

A Solution Path*

(0, 0) → (4, 0) → (1, 3)



2. Which algorithm gives the shortest path? Why?

BFS and A* both return the shortest path in terms of the number of steps.

BFS guarantees this by exploring all possibilities layer by layer.

A* guarantees it because it uses a heuristic function plus path cost, guiding the search toward the goal efficiently.

DFS does not guarantee the shortest path—it just finds a path, which can be much longer.


3. Which algorithm is more efficient in terms of time and memory?

Time Efficiency:

DFS is usually fast if the goal is found early, but it can waste time exploring deep irrelevant states.

BFS can take more time since it expands all nodes level by level.

A* is generally the most time-efficient because the heuristic guides the search and reduces unnecessary exploration.

Memory Efficiency:

DFS is the most memory-efficient—it only needs to store the path and visited states along one branch.

BFS is the least memory-efficient—it stores all states at the current level, which can grow exponentially.

A* needs more memory than DFS (it stores costs, heuristics, and open lists), but usually less than BFS if the heuristic is good.