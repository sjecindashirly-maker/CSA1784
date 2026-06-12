# Map Coloring Problem using CSP (Constraint Satisfaction Problem)

def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, assignment={}):
    # If all regions are assigned a color
    if len(assignment) == len(graph):
        return assignment

    # Select an unassigned region
    unassigned = [v for v in graph if v not in assignment]
    region = unassigned[0]

    # Try each color
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color

            result = map_coloring(graph, colors, assignment)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None

# Example map
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = map_coloring(graph, colors)

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution found")
