from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        next_states = [
            (cap1, y),                     # Fill Jug1
            (x, cap2),                     # Fill Jug2
            (0, y),                        # Empty Jug1
            (x, 0),                        # Empty Jug2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  # Jug1 -> Jug2
            (x + min(y, cap1 - x), y - min(y, cap1 - x))   # Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("No solution found.")

# Example
water_jug(4, 3, 2)
