# Alpha-Beta Pruning Algorithm

MAX, MIN = 1000, -1000

def alphabeta(depth, nodeIndex, maximizingPlayer,
              values, alpha, beta, maxDepth):

    # Base case: leaf node reached
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta Cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Cut-off
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

maxDepth = 3

result = alphabeta(0, 0, True, values,
                   MIN, MAX, maxDepth)

print("The optimal value is:", result)
