from collections import deque


def friend_distance(friends, userA, userB):
    """Returns the distance between userA and userB"""

    if userA == userB:
        return 0

    # Create a queue and list of visited users
    visited = {}
    queue = deque([(userA, 1)])  # (node, distance)

    # Iterate through the queue until it is empty
    while len(queue) > 0:
        curr_node, distance = queue.popleft()

        # Skip this user if we've already visited
        if curr_node in visited:
            continue
        visited[curr_node] = True

        # If this user is friends with userB, return
        if friends[curr_node][userB]:
            return distance

        # Enqueue new friends with increased distance
        for i in range(len(friends)):
            if friends[curr_node][i]:
                queue.append((i, distance + 1))

    return -1


# debug your code below
friends = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

print(friend_distance(friends, 0, 1))
print(friend_distance(friends, 1, 2))
print(friend_distance(friends, 0, 2))
print(friend_distance(friends, 0, 0))
