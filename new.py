network = {
    "S1": ["S2", "S3"],
    "S2": ["S1", "S3", "S4"],
    "S3": ["S1", "S2", "S4"],
    "S4": ["S2", "S3", "S5"],
    "S5": ["S4", "Gateway"],
    "Gateway": ["S5"]
}

from collections import deque


def find_route(network, start, destination):

    queue = deque()

    queue.append([start])

    visited = set()

    visited.add(start)

    while queue:

        route = queue.popleft()

        current = route[-1]

        if current == destination:
            return route

        for neighbor in network[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                new_route = route + [neighbor]

                queue.append(new_route)

    return None

route = find_route(
    network,
    "S1",
    "Gateway"
)

print("Route:", route)
