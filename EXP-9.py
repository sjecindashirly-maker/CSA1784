from itertools import permutations

# Distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = list(range(1, n))

min_cost = float('inf')
best_path = []

for path in permutations(cities):
    cost = 0
    current = 0

    for city in path:
        cost += graph[current][city]
        current = city

    cost += graph[current][0]  # Return to starting city

    if cost < min_cost:
        min_cost = cost
        best_path = (0,) + path + (0,)

print("Minimum Cost:", min_cost)
print("Optimal Path:", best_path)
