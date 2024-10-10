from typing import List, Optional


class Node:
    # Constructor to create a new node
    def __init__(self, cost: int):
        self.cost: int = cost
        self.children: List["Node"] = []
        self.parent: Optional["Node"] = None


# Honda wishes to find the minimal Sales Path cost in its distribution tree.
# Given a node rootNode, write a function getCheapestCost that calculates
# the minimal Sales Path cost in the tree.

# Complexity Time = O(V), where N = Node and M = Children
# TC = O(V), where V is number of vertices
# Space = O(N)
# Depth-First Search
# minPathSum = float("inf")
minPathSum = float("inf")


def dfs(rootNode: Node, cost: int):
    global minPathSum

    if not rootNode:
        return

    # rootNode.visited = True;
    cost += rootNode.cost

    for child in rootNode.children:
        # if not rootNode.visited:
        dfs(child, cost)

    if not rootNode.children:
        minPathSum = min(minPathSum, cost)


def get_cheapest_cost(rootNode: Node) -> int:

    # Approach: Depth-First Seach
    # Keep min cost sum
    global minPathSum

    minPathSum = float("inf")

    dfs(rootNode, 0)

    return minPathSum


# debug your code below
root = Node(0)
root.children = [Node(5), Node(3), Node(6)]
root.children[0].children = [Node(4), Node(2)]
root.children[1].children = [Node(0)]
root.children[2].children = [Node(1), Node(5)]

print(get_cheapest_cost(root))
